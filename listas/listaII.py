
class Pessoa: 
    def __init__(self, cpf, nome, idade, tipo_pessoa):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.tipo_pessoa = tipo_pessoa
        
    def get_data(self):
        return f"{self.cpf} \n{self.nome}"
                
    def eh_fumante(self):
        if self.tipo_pessoa == "F":
            return "É fumante"
        return "não fumante"

pessoa = Pessoa(32790762856, "Maíra", 37, "F")
print(pessoa.get_data())
print(pessoa.eh_fumante())


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade, tipo_pessoa):
        super().__init__(cpf, nome, idade, tipo_pessoa)
        
    def get_pessoa_fisica(self):
        return "É uma pessoa física"

pessoa_fisica = PessoaFisica(32790762856, "Maíra", 37, "N")
print(pessoa_fisica.get_pessoa_fisica())


class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome, idade, tipo_pessoa):
        self.cnpj = cnpj
        super().__init__(cnpj, nome, idade, tipo_pessoa)
        
    def get_cnpj(self):
        return self.cnpj

pessoa_juridica = PessoaJuridica(327907628000159, "MK-ME", 2, "F")
print(pessoa_juridica.get_cnpj())


class Professor:
    def __init__(self, nome, idade, salario):
        self.nome =  nome
        self.idade = idade
        self.salario = salario
    
    def __salario(self):
        return self.salario
    
    def ver_salario(self):
        if self.nome == "Ibere":
            return self.__salario()
        
adm = Professor("Ian", 31, 2.500)
print(adm.ver_salario())


class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area_quadrado(self):
        area = self.lado * self.lado
        return area
    
    def perimetro_quadrado(self):
        perimetro = self.lado * 4
        return perimetro

area_quadrado = Quadrado(2)
perimetro_quadrado = Quadrado(2)
print(area_quadrado.area_quadrado())
print(perimetro_quadrado.perimetro_quadrado())