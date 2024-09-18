from experta import *

caiuVar = False

# Define a fact class
class CareerFact(Fact):
    """Fact for career guidance."""
    pass

# Create the knowledge engine
class CareerExpert(KnowledgeEngine):

    @Rule(CareerFact(interesse='biologia', habilidades='laboratório', perfil='empatia'))
    def biology_science(self):
        print("Rule 1 triggered")
        self.resultado('Ciências Biológicas')

    @Rule(CareerFact(interesse='biologia', habilidades='pesquisa', perfil='comunicação'))
    def biology_science_2(self):
        print("Rule 2 triggered")
        self.resultado('Ciências Biológicas')

    @Rule(CareerFact(interesse='biologia', habilidades='observação', perfil='detalhista'))
    def biology_science_3(self):
        print("Rule 3 triggered")
        self.resultado('Ciências Biológicas')

    @Rule(CareerFact(interesse='química', habilidades='experimentos', perfil='metódico'))
    def exact_sciences(self):
        print("Rule 4 triggered")
        self.resultado('Ciências Exatas')

    @Rule(CareerFact(interesse='matemática', habilidades='análise', perfil='raciocínio lógico'))
    def exact_sciences_2(self):
        print("Rule 5 triggered")
        self.resultado('Ciências Exatas')

    @Rule(CareerFact(interesse='física', habilidades='problemas', perfil='teórico'))
    def exact_sciences_3(self):
        print("Rule 6 triggered")
        self.resultado('Ciências Exatas')

    @Rule(CareerFact(interesse='história', habilidades='pesquisa', perfil='comunicação'))
    def human_sciences(self):
        print("Rule 7 triggered")
        self.resultado('Ciências Humanas')

    @Rule(CareerFact(interesse='antropologia', habilidades='observação', perfil='empatia'))
    def human_sciences_2(self):
        print("Rule 8 triggered")
        self.resultado('Ciências Humanas')

    @Rule(CareerFact(interesse='psicologia', habilidades='escuta', perfil='empatia'))
    def human_sciences_3(self):
        print("Rule 9 triggered")
        self.resultado('Ciências Humanas')

    @Rule(CareerFact(interesse='política', habilidades='debate', perfil='argumentação'))
    def political_science(self):
        print("Rule 10 triggered")
        self.resultado('Ciências Políticas')

    @Rule(CareerFact(interesse='direito', habilidades='análise de casos', perfil='argumentação'))
    def political_science_2(self):
        print("Rule 11 triggered")
        self.resultado('Ciências Políticas')

    @Rule(CareerFact(interesse='economia', habilidades='análise de dados', perfil='raciocínio lógico'))
    def political_science_3(self):
        print("Rule 12 triggered")
        self.resultado('Ciências Políticas')

    @Rule(CareerFact(interesse='educação', habilidades='ensinar', perfil='didática'))
    def teaching(self):
        print("Rule 13 triggered")
        self.resultado('Licenciatura (Geral)')

    @Rule(CareerFact(interesse='educação física', habilidades='motivação', perfil='comunicação'))
    def teaching_2(self):
        print("Rule 14 triggered")
        self.resultado('Licenciatura (Geral)')

    @Rule(CareerFact(interesse='artes', habilidades='criatividade', perfil='expressão'))
    def teaching_3(self):
        print("Rule 15 triggered")
        self.resultado('Licenciatura (Geral)')

    @Rule(CareerFact(interesse='programação', habilidades='desenvolvimento', perfil='detalhista'))
    def computing(self):
        print("Rule 16 triggered")
        self.resultado('Computação')

    @Rule(CareerFact(interesse='redes', habilidades='gerenciamento', perfil='raciocínio lógico'))
    def computing_2(self):
        print("Rule 17 triggered")
        self.resultado('Computação')

    @Rule(CareerFact(interesse='inteligência artificial', habilidades='algoritmos', perfil='inovação'))
    def computing_3(self):
        print("Rule 18 triggered")
        self.resultado('Computação')

    # Additional Rules
    @Rule(CareerFact(interesse='medicina', habilidades='diagnóstico', perfil='empatia'))
    def biology_science_4(self):
        print("Rule 19 triggered")
        self.resultado('Ciências Biológicas')

    @Rule(CareerFact(interesse='veterinária', habilidades='tratamento', perfil='empatia'))
    def biology_science_5(self):
        print("Rule 20 triggered")
        self.resultado('Ciências Biológicas')

    @Rule(CareerFact(interesse='astronomia', habilidades='observação', perfil='detalhista'))
    def exact_sciences_4(self):
        print("Rule 21 triggered")
        self.resultado('Ciências Exatas')

    @Rule(CareerFact(interesse='engenharia', habilidades='projeto', perfil='prático'))
    def exact_sciences_5(self):
        print("Rule 22 triggered")
        self.resultado('Ciências Exatas')

    @Rule(CareerFact(interesse='literatura', habilidades='escrita', perfil='criatividade'))
    def human_sciences_4(self):
        print("Rule 23 triggered")
        self.resultado('Ciências Humanas')

    @Rule(CareerFact(interesse='filologia', habilidades='análise linguística', perfil='detalhista'))
    def human_sciences_5(self):
        print("Rule 24 triggered")
        self.resultado('Ciências Humanas')

    @Rule(CareerFact(interesse='direito internacional', habilidades='negociação', perfil='comunicação'))
    def political_science_4(self):
        print("Rule 25 triggered")
        self.resultado('Ciências Políticas')

    @Rule(CareerFact(interesse='administração pública', habilidades='gestão', perfil='organização'))
    def political_science_5(self):
        print("Rule 26 triggered")
        self.resultado('Ciências Políticas')

    @Rule(CareerFact(interesse='matemática aplicada', habilidades='modelagem', perfil='analítico'))
    def exact_sciences_6(self):
        print("Rule 27 triggered")
        self.resultado('Ciências Exatas')

    @Rule(CareerFact(interesse='economia', habilidades='modelagem econômica', perfil='detalhista'))
    def political_science_6(self):
        print("Rule 28 triggered")
        self.resultado('Ciências Políticas')

    @Rule(CareerFact(interesse='educação infantil', habilidades='didática', perfil='empatia'))
    def teaching_4(self):
        print("Rule 29 triggered")
        self.resultado('Licenciatura (Geral)')

    @Rule(CareerFact(interesse='educação superior', habilidades='pesquisa', perfil='acadêmico'))
    def teaching_5(self):
        print("Rule 30 triggered")
        self.resultado('Licenciatura (Geral)')

    @Rule(CareerFact(interesse='desenvolvimento de jogos', habilidades='programação', perfil='criatividade'))
    def computing_4(self):
        print("Rule 31 triggered")
        self.resultado('Computação')

    @Rule(CareerFact(interesse='segurança da informação', habilidades='criptografia', perfil='detalhista'))
    def computing_5(self):
        print("Rule 32 triggered")
        self.resultado('Computação')

    @Rule(CareerFact(interesse='botânica', habilidades='observação', perfil='detalhista'))
    def biology_science_6(self):
        print("Rule 33 triggered")
        self.resultado('Ciências Biológicas')

    @Rule(CareerFact(interesse='zoologia', habilidades='observação', perfil='empatia'))
    def biology_science_7(self):
        print("Rule 34 triggered")
        self.resultado('Ciências Biológicas')

    @Rule(CareerFact(interesse='engenharia de software', habilidades='desenvolvimento', perfil='raciocínio lógico'))
    def computing_6(self):
        print("Rule 35 triggered")
        self.resultado('Computação')

    @Rule(CareerFact(interesse='ciências ambientais', habilidades='pesquisa', perfil='empatia'))
    def biology_science_8(self):
        print("Rule 36 triggered")
        self.resultado('Ciências Biológicas')

    @Rule(CareerFact(interesse='economia aplicada', habilidades='análise estatística', perfil='raciocínio lógico'))
    def exact_sciences_7(self):
        print("Rule 37 triggered")
        self.resultado('Ciências Exatas')

    @Rule(CareerFact(interesse='direito ambiental', habilidades='análise de legislação', perfil='detalhista'))
    def political_science_7(self):
        print("Rule 38 triggered")
        self.resultado('Ciências Políticas')

    @Rule(CareerFact(interesse='educação musical', habilidades='ensinar', perfil='criatividade'))
    def teaching_6(self):
        print("Rule 39 triggered")
        self.resultado('Licenciatura (Geral)')

    @Rule(CareerFact(interesse='engenharia civil', habilidades='projeto', perfil='prático'))
    def exact_sciences_8(self):
        print("Rule 40 triggered")
        self.resultado('Ciências Exatas')

    def resultado(self, resultado):
        global caiuVar
        caiuVar = True
        print(f"\nResultado sugerido: {resultado}")

# Requesting input from the user
def get_user_input():
    interesse = input("Digite o seu interesse (ex: Biologia, Química, Matemática, etc.): ").strip().lower()
    habilidades = input("Digite a sua habilidade (ex: Pesquisa, Análise, Laboratório, etc.): ").strip().lower()
    perfil = input("Digite o seu perfil (ex: Comunicação, Empatia, Detalhista, etc.): ").strip().lower()
    return interesse, habilidades, perfil

# Create the engine and declare facts
engine = CareerExpert()
engine.reset()

# Get input from user
interesse, habilidades, perfil = get_user_input()

# Declare the fact based on user input
engine.declare(CareerFact(interesse=interesse, habilidades=habilidades, perfil=perfil))

# Run the engine
engine.run()

# If no rule was triggered, print a default message
if not caiuVar:
    print("Nenhuma sugestão encontrada com base nas informações fornecidas.")

input("Pressione Enter para sair...")