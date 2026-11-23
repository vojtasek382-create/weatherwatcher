from dataclasses import dataclass


@dataclass
class DataPocasi:
    mesto: str
    teplota: float
    pocitova_teplota: float
    vlhkost: int
    rychlost_vetru: float
    popis: str
    prsi: bool


@dataclass
class PravidloAktivity:
    nazev: str
    min_teplota: float
    max_teplota: float
    max_rychlost_vetru: float
    povolit_dest: bool

    def je_vhodne(self, pocasi: DataPocasi) -> bool:
        if pocasi.prsi and not self.povolit_dest:
            return False
        if not (self.min_teplota <= pocasi.teplota <= self.max_teplota):
            return False
        if pocasi.rychlost_vetru > self.max_rychlost_vetru:
            return False
        return True
