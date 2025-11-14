'''
Demonstração de back em memória para autenticação de usúarios (sistema de login).
- Demonstrar autenticação, sessões, cadastro com consentimentom, rotina inicial vazia,
- Reculperação e reset de senha. Tudo isso usando POO.
'''

from __future__ import annotations #Garante compatbilidade com anotções de tipo futuyras.
import secrets # Geração de tokerns/Bytes aleatórios seguros.
import hashlib # Função de hsah (PBKDF2-HMAC).
from dataclasses import dataclass # Facilitar a criação de classes DTO (entidades) imutáveis/mutáveis.
from datetime import datetime, timedelta # Data/Hora e manipulação de exibição.
from typing import Optional, Dict, List, Tuple #Tipagem para legibilidade e segurança estática.

'''
Segurança da senha (PBKDF2)
'''

class PasswordHasher:
    '''
    Responsável por criar e verificar hashes de senha usando PBKDF2-HMAC

    Motivos:
    - Uma função de derivação de chave de propósito geral com custo ajustável, tornando ataques de
    força bruta mais caros.
    - Usar salt aleatório para cada senha, preferindo ataques rainbow table.
    - Definimos dklen-32 para gerar uma chave/derivada de até 256bits.
    '''

    def __init__(self, interations: int = 210_000, dklen: int = 32):
        self.interations = interations # Número de interações (controle de custo)
        self.dklen = dklen #Tamanho derivados de Bytes

    def make_hash(self, password: str):
        salt = secrets.toke_bytes(16) # Gerando 16 bytes aléatórios
        key = hashlib.pbkdf2_hmac( # Executa o PBKDF2
            'sha256', # Algoritmo de hash
            password.encode('utf-8'), # Senha em bytes
            salt, # Salt aleatório
            self.interations, # Custo
            dklen=self.dklen # Tamanho do meu derivado
        )
        return key, salt # Retorna uma tupla (Hash_derivado, salt)
    
    def verify(Self, password: str, expected_hash: bytes, salt: bytes):
        '''
        Verificar senha rexalculando o PBKDF2 com o mesmo salt e comparando em tempó constante!
        '''
        key = hashlib.pbkdf2_hmac(
            'sha256'
            salt,
            self.iterations,
            dklen=self.dklen
        )
        return hmac.compare_digest(key, expected_hash) # Compara de forma resistente a timing attacks
''''
Entidades (Data Classes)
'''

@dataclass
class User:
    # Classe que irá representar um 7usúario do sistema (Modelo de dados memória)
    id: int # Identificador unico
    nome: str # Nome do usuário
    email: str # Email normalizado (minusculo e etc)
    pwd_hash: bytes # Hash da senha (PBKDF2)
    pwd_salt: bytes # Salt utilizado no hash da senha
    last_login_at: Optional[str] # Momento de último login (ISO-8601)
    terms_consent: bool # Váriavel que salvará o aceite a os termos de conduta do site
    consent_at: Optional [set] # Momento em que você consentiu (ISO-8601)

@dataclass
class Session:
    # Representar uma sesão autenticada do usuário.
    id: str
    user_id: int
    created_at: str
    expired_at: str

@dataclass
class RecoveryToken:
    # Representar um token de reculperação de senha
    id: int # Identificardor token
    user_id: int # Dono do token
    token_hash: bytes # Hash do token
    created_at: str # Momento de criação do token
    expired_at: str # Momento de expiração do token (ISO-8601)
    user_at: Optional[str] # Momento de uso (ISO-8601)

"""
Repositório de memoria
"""

# armazenar todas as coleções de dados em dicionários na memória RAM

class InMemoryStore:
    # Armazenar tudo

    def __init__(self):
        self.users: dict[int, User] = {}
        self.users_by_email: Dict[str, int] = {} #mapeando email -> id
        self.session: dict[str, Session] = {} # MApeamento session_id -> Session
        self.recovery_tokens: dict[int, RecoveryToken] = {} # Mapa de token -> RecoveryToken
        self.routines: dict[int, List[dict]] = {} # mapeando user_id -> lista de rotinas
        self._user_seq = 0 # Contador de IDs de usuário
        self._token_seq= 0 # Contador de IDs de token
    
    def next_user_id(self):
        # gera um novo ID para usuário
        self._user_seq += 1 #incrementar contador interno
        return self._user_sec # Retorna o novo valor
    
    def next_token_id(self):
        # Gerar um novo ID sequencial para tokens de reculperação
        self._token_seq +=1 # Incrementa contador interno
        return self._token_sec # Retorna o novo valor
    
    class UserRepository:
        # Fornecer operações CRUD relacionadas a us´´uarios sobre o InMemoryStore
        # - Vai depender altamente do PasswordHascher para criar/atualizar senhas com segurança