from abc import ABC, abstractmethod

# Interface para aprovação de exames
class Exame(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def verificar_condicoes(self):
        pass


# Implementação para exame de sangue
class ExameSangue(Exame):
    def __init__(self):
        super().__init__("sangue")

    def verificar_condicoes(self):
        # Lógica específica para exame de sangue
        return True


# Implementação para exame de raio-x
class ExameRaioX(Exame):
    def __init__(self):
        super().__init__("raio-x")

    def verificar_condicoes(self):
        # Lógica específica para exame de raio-x
        return True


# Classe responsável por aprovar exames
class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        if exame.verificar_condicoes():
            print(f"Exame {exame.tipo} aprovado!")
        else:
            print(f"Exame {exame.tipo} reprovado!")


# Exemplo de uso:
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)
