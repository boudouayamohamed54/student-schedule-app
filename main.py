import os
import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window


class StudentDatabase:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    level TEXT NOT NULL,
                    group_code TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def add_student(self, full_name: str, level: str, group_code: str):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (full_name, level, group_code) VALUES (?, ?, ?)",
                (full_name.strip(), level.strip(), group_code.strip()),
            )
            conn.commit()

    def update_student(self, student_id: int, full_name: str, level: str, group_code: str):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE students
                SET full_name = ?, level = ?, group_code = ?
                WHERE id = ?
                """,
                (full_name.strip(), level.strip(), group_code.strip(), student_id),
            )
            conn.commit()

    def get_students(self, search_query: str = ""):
        query = search_query.strip()
        with self._connect() as conn:
            cursor = conn.cursor()
            if query:
                cursor.execute(
                    """
                    SELECT id, full_name, level, group_code
                    FROM students
                    WHERE full_name LIKE ?
                    ORDER BY id DESC
                    """,
                    (f"%{query}%",),
                )
            else:
                cursor.execute(
                    "SELECT id, full_name, level, group_code FROM students ORDER BY id DESC"
                )
            return cursor.fetchall()

    def delete_student(self, student_id: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()


class StudentManagerUI(BoxLayout):
    def __init__(self, db: StudentDatabase, **kwargs):
        super().__init__(orientation="vertical", padding=12, spacing=10, **kwargs)
        self.db = db

        title_label = Label(
            text="Student Database Manager",
            font_size="22sp",
            bold=True,
            size_hint_y=None,
            height=45,
        )
        self.add_widget(title_label)

        # Form inputs for adding a new student
        form_grid = GridLayout(cols=1, spacing=8, size_hint_y=None, height=160)
        self.name_input = TextInput(
            hint_text="Full Name (e.g. Amine Benali)",
            multiline=False,
            size_hint_y=None,
            height=45,
        )
        self.level_input = TextInput(
            hint_text="Level / Specialty (e.g. L1 MI)",
            multiline=False,
            size_hint_y=None,
            height=45,
        )
        self.group_input = TextInput(
            hint_text="Group / Section (e.g. G2)",
            multiline=False,
            size_hint_y=None,
            height=45,
        )
        form_grid.add_widget(self.name_input)
        form_grid.add_widget(self.level_input)
        form_grid.add_widget(self.group_input)
        self.add_widget(form_grid)

        # Add & Refresh buttons
        btn_row = BoxLayout(size_hint_y=None, height=46, spacing=10)
        add_btn = Button(text="Add Student", background_color=(0.18, 0.55, 0.34, 1))
        add_btn.bind(on_press=self.on_add_student)

        refresh_btn = Button(text="Show All", background_color=(0.20, 0.45, 0.75, 1))
        refresh_btn.bind(on_press=self.on_reset_search)

        btn_row.add_widget(add_btn)
        btn_row.add_widget(refresh_btn)
        self.add_widget(btn_row)

        # Search bar by name
        search_row = BoxLayout(size_hint_y=None, height=44, spacing=8)
        self.search_input = TextInput(
            hint_text="Search by student name...",
            multiline=False,
        )
        self.search_input.bind(text=self.on_search_text)
        clear_search_btn = Button(
            text="Clear",
            size_hint_x=None,
            width=75,
            background_color=(0.45, 0.45, 0.50, 1),
        )
        clear_search_btn.bind(on_press=self.on_reset_search)
        search_row.add_widget(self.search_input)
        search_row.add_widget(clear_search_btn)
        self.add_widget(search_row)

        # Scrollable list of students
        self.list_container = BoxLayout(
            orientation="vertical", spacing=8, size_hint_y=None
        )
        self.list_container.bind(minimum_height=self.list_container.setter("height"))

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.list_container)
        self.add_widget(scroll)

        self.refresh_students()

    def show_message(self, title: str, message: str):
        content = BoxLayout(orientation="vertical", padding=10, spacing=10)
        content.add_widget(Label(text=message))
        close_btn = Button(text="OK", size_hint_y=None, height=42)
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.35))
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        popup.open()

    def open_edit_popup(self, student_id: int, full_name: str, level: str, group_code: str):
        layout = BoxLayout(orientation="vertical", padding=12, spacing=8)

        edit_name = TextInput(text=full_name, hint_text="Full Name", multiline=False, size_hint_y=None, height=44)
        edit_level = TextInput(text=level, hint_text="Level", multiline=False, size_hint_y=None, height=44)
        edit_group = TextInput(text=group_code, hint_text="Group", multiline=False, size_hint_y=None, height=44)

        layout.add_widget(edit_name)
        layout.add_widget(edit_level)
        layout.add_widget(edit_group)

        actions = BoxLayout(size_hint_y=None, height=44, spacing=8)
        save_btn = Button(text="Save", background_color=(0.18, 0.55, 0.34, 1))
        cancel_btn = Button(text="Cancel", background_color=(0.55, 0.25, 0.25, 1))

        popup = Popup(title=f"Edit Student #{student_id}", content=layout, size_hint=(0.9, 0.55))

        def save_changes(instance):
            new_name = edit_name.text.strip()
            new_level = edit_level.text.strip()
            new_group = edit_group.text.strip()
            if not new_name or not new_level or not new_group:
                self.show_message("Missing Data", "All fields are required.")
                return
            self.db.update_student(student_id, new_name, new_level, new_group)
            popup.dismiss()
            self.refresh_students(self.search_input.text)

        save_btn.bind(on_press=save_changes)
        cancel_btn.bind(on_press=popup.dismiss)

        actions.add_widget(save_btn)
        actions.add_widget(cancel_btn)
        layout.add_widget(actions)

        popup.open()

    def on_add_student(self, instance):
        full_name = self.name_input.text.strip()
        level = self.level_input.text.strip()
        group_code = self.group_input.text.strip()

        if not full_name or not level or not group_code:
            self.show_message("Missing Data", "Please fill in all fields.")
            return

        self.db.add_student(full_name, level, group_code)
        self.name_input.text = ""
        self.level_input.text = ""
        self.group_input.text = ""
        self.refresh_students(self.search_input.text)

    def on_search_text(self, instance, value):
        self.refresh_students(value)

    def on_reset_search(self, instance):
        self.search_input.text = ""
        self.refresh_students("")

    def on_delete_student(self, student_id: int):
        self.db.delete_student(student_id)
        self.refresh_students(self.search_input.text)

    def refresh_students(self, search_query: str = ""):
        self.list_container.clear_widgets()
        students = self.db.get_students(search_query)

        if not students:
            msg = (
                "No matching students found."
                if search_query.strip()
                else "No students in database yet."
            )
            self.list_container.add_widget(
                Label(text=msg, size_hint_y=None, height=40)
            )
            return

        for student_id, full_name, level, group_code in students:
            row = BoxLayout(size_hint_y=None, height=55, spacing=6)
            info_label = Label(
                text=f"#{student_id} | {full_name} ({level} - {group_code})",
                halign="left",
                valign="middle",
                text_size=(Window.width * 0.52, None),
            )
            edit_btn = Button(
                text="Edit",
                size_hint_x=None,
                width=65,
                background_color=(0.82, 0.55, 0.15, 1),
            )
            edit_btn.bind(
                on_press=lambda instance, sid=student_id, fn=full_name, lv=level, gp=group_code: self.open_edit_popup(
                    sid, fn, lv, gp
                )
            )

            del_btn = Button(
                text="Delete",
                size_hint_x=None,
                width=75,
                background_color=(0.75, 0.22, 0.22, 1),
            )
            del_btn.bind(
                on_press=lambda instance, sid=student_id: self.on_delete_student(sid)
            )

            row.add_widget(info_label)
            row.add_widget(edit_btn)
            row.add_widget(del_btn)
            self.list_container.add_widget(row)


class StudentScheduleApp(App):
    def build(self):
        os.makedirs(self.user_data_dir, exist_ok=True)
        db_path = os.path.join(self.user_data_dir, "students.db")
        db = StudentDatabase(db_path)
        return StudentManagerUI(db=db)


if __name__ == "__main__":
    StudentScheduleApp().run()