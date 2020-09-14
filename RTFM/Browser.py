"""
Author: Ari24
Name: RTFM
Description: Package for RTFM
License: MIT
Programmed in: IDLE :lul:

Hav fun, because this is good
"""

languages = {
    "de": "MINJUNG, LES DIE VERDAMMTEN DOCS ODER DU WIRST GEFEUERT!",
    "en": "DUDE, JUST READ THE FUCKING DOCS OR YOUR BOSS WILL FIRE YOU!",
    "fr": "MON GARÇON, LIS JUSTE CETTE PUTAIN DE DOCUMENTATION OU TON PATRON VA TE VIRER !",
    "esp": "CHICO, SÓLO LEE LA MALDITA DOCUMENTACIÓN O TU JEFE TE DESPEDIRÁ.",
    "ita": "RAGAZZO, LEGGI QUELLA CAZZO DI DOCUMENTAZIONE O IL TUO CAPO TI LICENZIERÀ!",
    "rus": "ПАРЕНЬ, ПРОСТО ПРОЧИТАЙ ЕБУЧУЮ ДОКУМЕНТАЦИЮ, ИЛИ ТВОЙ БОСС ТЕБЯ УВОЛИТ!",
    "jp": "おい、説明書を読まないと上司にクビにされるぞ！",
    "pol": "CHŁOPCZE, PO PROSTU PRZECZYTAJ TĘ PIEPRZONĄ DOKUMENTACJĘ, ALBO SZEF CIĘ ZWOLNI!",
    "nl": "JONGEN, LEES GEWOON DE VERDOMDE DOCUMENTATIE OF JE BAAS ZAL JE ONTSLAAN!"
}

class Google:
    def __init__(self, question="stupid question, dont ask me", lang="de"):
        self.question = question

        assert lang in languages
        
        self.lang = lang

    def RTFM(self):
        return languages[self.lang]
