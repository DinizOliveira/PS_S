from typing import Type
from enum import Enum, auto

class Projeto():

    def __init__(self, nomeProjeto: str, nomeCliente: str, nomeRevenda: str) -> None:
        self.__nomeProjeto = nomeProjeto
        self.__nomeCliente = nomeCliente
        self.__nomeRevenda = nomeRevenda
        self.__ambientes = Ambiente()


class Ambiente():

    def __init__(self, codigo: int, nome: str) -> object:
        self.__codigo = codigo
        self.__nome = nome
        self.__listaItens = ItemAmbiente()


class ItemAmbiente():

    def __init__(self, codigo: int, nome: str, ambientePai: Type[Ambiente]) -> object:
        self._codigo = codigo
        self._nome = nome 
        self._ambientePai = ambientePai


class ETipoLuminaria(Enum):

    FLUORESCENTE = auto()
    HALÓGENA = auto()
    INCANDESCENTE = auto()
    LED = auto()


class Ecor(Enum):

    AZUL = auto()
    PRATA = auto()
    PRETO = auto()
    CINZA = auto() 


class Modulos(ItemAmbiente):

    def __init__(self, codigo: int, nome: str, ambientePai: Type[Ambiente], qtdCanais: int, iluminarias: Type[ETipoLuminaria]) -> None:
        super().__init__(codigo, nome, ambientePai)
        self.__qtdCanais = qtdCanais
        self.__iluminarias = iluminarias


class Luminaria(ItemAmbiente):

    def __init__(self, codigo: int, nome: str, ambientePai: Type[Ambiente], tipoLuminaria: Type[ETipoLuminaria], potencia: int) -> None:
        super().__init__(codigo, nome, ambientePai)
        self.__tipoLuminaria = tipoLuminaria
        self.__potencia = potencia
  

class Teclado(ItemAmbiente):

    def __init__(self, codigo: int, nome: str, ambientePai: Type[Ambiente], cor: Type[Ecor], possuiSensor: bool) -> None:
        super().__init__(codigo, nome, ambientePai)
        self.__teclas = Tecla()
        self.__cor = cor
        self.__possuiSensor = possuiSensor
        

class Tecla():

    def __init__(self, nome: str, luminaria: Type[Luminaria]) -> object:
        self.__nome = nome 
        self.__luminaria = luminaria
