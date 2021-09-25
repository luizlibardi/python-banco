from utils.helper import formata_float_str_moeda

class Conta:
    id: int = 1

    def __init__(self: object, nome: str, saldo: float, limite: int) -> None:
        self.__codigo: int = Conta.id
        self.__nome: str = nome
        self.__saldo: float = saldo
        self.__limite: int = limite
        Conta.id += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def saldo(self: object) -> float:
        return self.__saldo
    
    @property
    def limite(self: object) -> float:
        return self.__limite

    def __str__(self) -> str:
        return f'Código da Conta: {self.codigo} \nNome: {self.nome} \nSaldo: {formata_float_str_moeda(self.saldo)} Limite: {self.limite}'