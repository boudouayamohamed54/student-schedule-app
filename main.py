import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup

students_db = [
    {"nom": "ABBES", "prenom": "ABIR MERIEM", "groupe": "G1"},
    {"nom": "ABDELDJEBAR", "prenom": "CHAHINEZ", "groupe": "G1"},
    {"nom": "ABDELLI", "prenom": "Selma", "groupe": "G1"},
    {"nom": "ADDA", "prenom": "MALEK", "groupe": "G1"},
    {"nom": "ADDOU", "prenom": "ALI ILYAS", "groupe": "G1"},
    {"nom": "ADEL", "prenom": "FERYAL", "groupe": "G1"},
    {"nom": "AFCIL", "prenom": "Imene", "groupe": "G1"},
    {"nom": "AIT YALA", "prenom": "HAMAMA", "groupe": "G1"},
    {"nom": "AKKAL", "prenom": "Mohammed Reda", "groupe": "G1"},
    {"nom": "ZEDDOUR MOHAMMEDI", "prenom": "CHEIMA", "groupe": "G1"},
    {"nom": "ARRAS", "prenom": "Sara Salsabil", "groupe": "G1"},
    {"nom": "ATHEMANI", "prenom": "SALSABIL", "groupe": "G1"},
    {"nom": "BACHIR", "prenom": "HADIL", "groupe": "G1"},
    {"nom": "BARKAOUI", "prenom": "MARWA", "groupe": "G1"},
    {"nom": "BARKAT", "prenom": "Souad", "groupe": "G1"},
    {"nom": "BELGHERBI", "prenom": "REKIA", "groupe": "G1"},
    {"nom": "BELHADJ", "prenom": "MERIEM FERIAL", "groupe": "G1"},
    {"nom": "BELLAH", "prenom": "FATMA", "groupe": "G1"},
    {"nom": "BEN MAHIDI", "prenom": "AICHA", "groupe": "G1"},
    {"nom": "BENCHIHA", "prenom": "SIHEM", "groupe": "G1"},
    {"nom": "BENABDELKADER", "prenom": "ROMAISSA EZOHHRA", "groupe": "G1"},
    {"nom": "BENDJEDDA", "prenom": "WISSEM HALIMA", "groupe": "G1"},
    {"nom": "BENAISSA", "prenom": "KELTOUM", "groupe": "G1"},

    {"nom": "BENAZZOUZ", "prenom": "KHEIRA AMINA", "groupe": "G2"},
    {"nom": "BENGOUA", "prenom": "MAROUA", "groupe": "G2"},
    {"nom": "BENSAIDI", "prenom": "IKRAM", "groupe": "G2"},
    {"nom": "BENSMICHA", "prenom": "FATIMA ZOHRA RAHMA", "groupe": "G2"},
    {"nom": "BENTENNI", "prenom": "Maroua", "groupe": "G2"},
    {"nom": "BENYAKHOU", "prenom": "ALAA", "groupe": "G2"},
    {"nom": "BENYAMINA", "prenom": "Manal", "groupe": "G2"},
    {"nom": "BOUARFA", "prenom": "ARIDJ RANIM REKIA", "groupe": "G2"},
    {"nom": "BOUCHENAFA", "prenom": "SENDOUS NARIMANE", "groupe": "G2"},
    {"nom": "BOUCHENTOUF", "prenom": "DOUAA SAKINA", "groupe": "G2"},
    {"nom": "BOUCHERIH", "prenom": "Nour El Houda", "groupe": "G2"},
    {"nom": "BOUDAOUD", "prenom": "Fares Abdelilah", "groupe": "G2"},
    {"nom": "BOUDOUAYA", "prenom": "YOUCEF MOHAMMED", "groupe": "G2"},
    {"nom": "BOUHAOUS", "prenom": "MERIEM", "groupe": "G2"},
    {"nom": "BOUKEHILI", "prenom": "RADIA MANEL", "groupe": "G2"},
    {"nom": "BOUKHALFA", "prenom": "Feriel Insaf", "groupe": "G2"},
    {"nom": "BOUKHATEM", "prenom": "Sara", "groupe": "G2"},
    {"nom": "BOUMEDIENE", "prenom": "MAROUA", "groupe": "G2"},
    {"nom": "BOUMERSDJED", "prenom": "MOHAMED SIRADJ EDDINE", "groupe": "G2"},
    {"nom": "BERRAHOU", "prenom": "FAROUK", "groupe": "G2"},
    {"nom": "BOUMESJED", "prenom": "AYA", "groupe": "G2"},

    {"nom": "BOUNOUARA", "prenom": "DHOHA MERIEM", "groupe": "G3"},
    {"nom": "BOUROUMEID", "prenom": "HAYET", "groupe": "G3"},
    {"nom": "BOUSSAYED", "prenom": "Imene Ahlem", "groupe": "G3"},
    {"nom": "BOUZOUIRA", "prenom": "IMENE", "groupe": "G3"},
    {"nom": "CHAFI", "prenom": "MAAMAR IBRAHIM", "groupe": "G3"},
    {"nom": "CHAHED", "prenom": "MANEL", "groupe": "G3"},
    {"nom": "CHAREF", "prenom": "YOUSRA", "groupe": "G3"},
    {"nom": "CHEBAB", "prenom": "Mohammed", "groupe": "G3"},
    {"nom": "CHERCHAB", "prenom": "Douaa Fatiha", "groupe": "G3"},
    {"nom": "CHOUCHA", "prenom": "Besmala Hanaa", "groupe": "G3"},
    {"nom": "DAOUD", "prenom": "KAWTHER", "groupe": "G3"},
    {"nom": "DELBAZE", "prenom": "Abdessamad", "groupe": "G3"},
    {"nom": "DERRICHE", "prenom": "Douaa Kheira", "groupe": "G3"},
    {"nom": "DIDA", "prenom": "AHLEM", "groupe": "G3"},
    {"nom": "DIDI", "prenom": "KAMEL ABDERRACHID", "groupe": "G3"},
    {"nom": "DJAOUT", "prenom": "Chemss Edoha", "groupe": "G3"},
    {"nom": "FERHAT", "prenom": "Douaa Fatima Zohra", "groupe": "G3"},
    {"nom": "DOUMA", "prenom": "SOHAIB", "groupe": "G3"},
    {"nom": "ELAHMAR", "prenom": "RANIA HIDAYET", "groupe": "G3"},
    {"nom": "KARI", "prenom": "Maram", "groupe": "G3"},
    {"nom": "ENNEMICHE", "prenom": "Aya Yasmine", "groupe": "G3"},
    {"nom": "EZZINE", "prenom": "Farah", "groupe": "G3"},

    {"nom": "FEKIR", "prenom": "YAHIA BARAA", "groupe": "G4"},
    {"nom": "DJOUHRI", "prenom": "KAWTHER", "groupe": "G4"},
    {"nom": "GAMRA", "prenom": "Mouad Abde Illah", "groupe": "G4"},
    {"nom": "GARAOUI", "prenom": "Khaoula", "groupe": "G4"},
    {"nom": "GUERANDI", "prenom": "Wissal Farah", "groupe": "G4"},
    {"nom": "HAKEMI", "prenom": "WARDA HIBAT ERRAHMANI", "groupe": "G4"},
    {"nom": "HAMIDAT", "prenom": "Chaimaa", "groupe": "G4"},
    {"nom": "HEIRECHE", "prenom": "Assia Imene", "groupe": "G4"},
    {"nom": "HEIRECHE", "prenom": "CHIRAZ CHAHLA", "groupe": "G4"},
    {"nom": "HENIEN DJELLOUL", "prenom": "Zahra El Yasmine", "groupe": "G4"},
    {"nom": "HERRATI", "prenom": "HAFEDA", "groupe": "G4"},
    {"nom": "KAHLOUCHE", "prenom": "Meriem", "groupe": "G4"},
    {"nom": "KENNANE", "prenom": "RAZIKA", "groupe": "G4"},
    {"nom": "KHENNOUS", "prenom": "Nadjat", "groupe": "G4"},
    {"nom": "KINA", "prenom": "Khalida Aicha", "groupe": "G4"},
    {"nom": "KOURAT", "prenom": "Imene Racha Romeissaa", "groupe": "G4"},
    {"nom": "KOURDASSI", "prenom": "FARAH", "groupe": "G4"},
    {"nom": "LARDJANE", "prenom": "Mohamed El Amine", "groupe": "G4"},
    {"nom": "LASSAB", "prenom": "NESRINE", "groupe": "G4"},
    {"nom": "SEDDAR", "prenom": "NOUR EL HOUDA", "groupe": "G4"},
    {"nom": "KEMIG", "prenom": "KAOUTAR", "groupe": "G4"},
    {"nom": "LATRECHE", "prenom": "HIBA INSAF", "groupe": "G4"},

    {"nom": "BEKHEDDA", "prenom": "HAFEDA", "groupe": "G5"},
    {"nom": "LEGRA", "prenom": "Mohammed Abdelhak", "groupe": "G5"},
    {"nom": "MAMOUNI", "prenom": "MOHAMMED EL AMINE", "groupe": "G5"},
    {"nom": "MEBARKI", "prenom": "MAROUA OUM HANI", "groupe": "G5"},
    {"nom": "MEDDAH", "prenom": "MOHAMMED NOUR EL ISLEM", "groupe": "G5"},
    {"nom": "MEDJADJI", "prenom": "RIHEB MEISSAA", "groupe": "G5"},
    {"nom": "MEDJAHDI", "prenom": "HIBAT ELLAH BESMALA", "groupe": "G5"},
    {"nom": "MELLAH", "prenom": "MERYEM", "groupe": "G5"},
    {"nom": "MENEZLA", "prenom": "CHOUROUKHIBET ERRAHMENE", "groupe": "G5"},
    {"nom": "MESSADAOUI", "prenom": "Amina", "groupe": "G5"},
    {"nom": "MISSOURI", "prenom": "Imane", "groupe": "G5"},
    {"nom": "MOHAMMEDI", "prenom": "MALIKA", "groupe": "G5"},
    {"nom": "MOULELFARA", "prenom": "IKRAM", "groupe": "G5"},
    {"nom": "NASRI", "prenom": "Bensekrane Mohammed El Amine", "groupe": "G5"},
    {"nom": "NEDJADI", "prenom": "HADJER", "groupe": "G5"},
    {"nom": "OTMANE", "prenom": "HADIL MALAK", "groupe": "G5"},
    {"nom": "OUAFI", "prenom": "Aya Ines", "groupe": "G5"},
    {"nom": "OUGGAD", "prenom": "Farah", "groupe": "G5"},
    {"nom": "OUKID", "prenom": "AMINA", "groupe": "G5"},
    {"nom": "OURNIDI", "prenom": "WASSILA", "groupe": "G5"},
    {"nom": "OURRAD", "prenom": "NOUSSAIBA", "groupe": "G5"},
    {"nom": "OURRED", "prenom": "Mohammed Nadjib", "groupe": "G5"},

    {"nom": "RAGUED", "prenom": "MOHAMMED ABDEL ILAH", "groupe": "G6"},
    {"nom": "RAOUTI", "prenom": "Yamina", "groupe": "G6"},
    {"nom": "ROGUI", "prenom": "MAROUA TORKIA", "groupe": "G6"},
    {"nom": "SAHIH", "prenom": "NOUR EL HOUDA", "groupe": "G6"},
    {"nom": "SAHNINE", "prenom": "FATIMA ZOHRA", "groupe": "G6"},
    {"nom": "SALHI", "prenom": "MANAL", "groupe": "G6"},
    {"nom": "SEBIA", "prenom": "Rihem", "groupe": "G6"},
    {"nom": "SEHLI", "prenom": "Nounia", "groupe": "G6"},
    {"nom": "SEKKAI", "prenom": "Mohammed", "groupe": "G6"},
    {"nom": "SENHADJI", "prenom": "Khadidja", "groupe": "G6"},
    {"nom": "SOUAFI", "prenom": "Hanâ", "groupe": "G6"},
    {"nom": "SOUDINI", "prenom": "AL AIDIA HANANE", "groupe": "G6"},
    {"nom": "TEFIANI", "prenom": "DOUAA KHADIDJA", "groupe": "G6"},
    {"nom": "TOUHAMI", "prenom": "YASSMINE FATIMA ZOHRA", "groupe": "G6"},
    {"nom": "YAMANI", "prenom": "Wassila", "groupe": "G6"},
    {"nom": "YASSINE", "prenom": "AMINA", "groupe": "G6"},
    {"nom": "ZAIR", "prenom": "ASMA ZOUBIDA", "groupe": "G6"},
    {"nom": "AMAR", "prenom": "CHAIMAA", "groupe": "G6"},
    {"nom": "SADI", "prenom": "ANFAL", "groupe": "G6"},
    {"nom": "ISSAD", "prenom": "MOHAMMED ANIS", "groupe": "G6"},
    {"nom": "ZEKRI", "prenom": "INES", "groupe": "G6"}
]

class StudentApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        root_layout.add_widget(Label(text="Recherche de Groupe (1ère Année)", size_hint_y=None, height=50, font_size=20))
        
        search_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.search_input = TextInput(hint_text="Entrez le nom ou prénom...", multiline=False, font_size=16)
        self.search_input.bind(text=self.on_search_text)
        
        search_btn = Button(text="Afficher", size_hint_x=None, width=110, background_color=(0.17, 0.24, 0.31, 1))
        search_btn.bind(on_press=self.submit_search)
        
        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_btn)
        root_layout.add_widget(search_layout)
        
        self.results_scroll = ScrollView()
        self.results_layout = GridLayout(cols=1, spacing=8, size_hint_y=None)
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))
        self.results_scroll.add_widget(self.results_layout)
        root_layout.add_widget(self.results_scroll)
        
        self.status_label = Label(text="Tapez le nom pour rechercher...", size_hint_y=None, height=35, color=(0.5, 0.5, 0.5, 1))
        root_layout.add_widget(self.status_label)
        
        return root_layout

    def on_search_text(self, instance, value):
        self.update_results(value)

    def update_results(self, query):
        self.results_layout.clear_widgets()
        query = query.strip().upper()
        if not query:
            self.status_label.text = "Tapez le nom pour rechercher..."
            return
        
        matches = [s for s in students_db if query in s["nom"].upper() or query in s["prenom"].upper()]
        self.status_label.text = f"Résultats trouvés : {len(matches)}"
        
        for s in matches:
            btn_text = f"{s['nom']} {s['prenom']} ({s['groupe']})"
            btn = Button(text=btn_text, size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.8, 1))
            btn.bind(on_press=lambda instance, student=s: self.open_schedule(student))
            self.results_layout.add_widget(btn)

    def submit_search(self, instance):
        query = self.search_input.text.strip().upper()
        matches = [s for s in students_db if query in s["nom"].upper() or query in s["prenom"].upper()]
        if matches:
            self.open_schedule(matches[0])

    def open_schedule(self, student):
        groupe = student["groupe"]
        img_path = f"{groupe}.jpg"
        if not os.path.exists(img_path):
            img_path = f"{groupe}.png"
            
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        if os.path.exists(img_path):
            img = Image(source=img_path, allow_stretch=True)
            content.add_widget(img)
        else:
            content.add_widget(Label(text=f"Image {groupe}.jpg introuvable !"))
            
        close_btn = Button(text="Fermer", size_hint_y=None, height=50, background_color=(0.8, 0.2, 0.2, 1))
        content.add_widget(close_btn)
        
        popup = Popup(
            title=f"Emploi du temps - {groupe} ({student['nom']} {student['prenom']})",
            content=content,
            size_hint=(0.95, 0.95)
        )
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    StudentApp().run()
