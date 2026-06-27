# #diketahui: 
# mula-mula CoG dan P (moncong) tingginya sama = 100m
# jarak P - CoG = 3m
# garis P - CoG sejajar dan berhimpit dengan garis Bx, dapat dikatakan P berada di koordinat (3,0,0)
# ada angin meniup dari depan dan kanan
# sehingga body pesawat berotasi 30* terhadap sumbu nO, dengan n = (4,-3,0) terhadap kerangka body B

# ditanya:
# a. Posisi akhir P pada koordinat kerangka body setelah rotasi
# b. ketinggian P terhadap permukaan bumi

import numpy as np
from pyquaternion import Quaternion

class Solusi:
    def __init__(self, titik: list[int], rotasi: list[int], teta: float) -> None:
        self.titik_list = titik[1:]
        self.titik_array = np.array(titik)
        self.rotasi = rotasi
        self.teta = teta

    def to_radian(self, teta: float):
        return np.radians(teta)

    def convert_q_bar(self, rotasi: list[int], teta: float):
        return Quaternion(axis=rotasi, angle=self.to_radian(teta))

    def convert_q_conjugate(self, q_bar):
        return q_bar.conjugate
    
    def v1_titik_hasil(self, titik_array: np.ndarray, q_bar, q_conjugate):
        P2 = q_bar * titik_array * q_conjugate
        return P2 
    
    def v2_titik_hasil(self, titik_list: list[int], q_bar):
        v2P2 = q_bar.rotate(titik_list)
        return v2P2
    
def cari_tinggi(titik_p: list[float], tinggi_mula: int) -> float:
    tinggi_dari_tanah: float = tinggi_mula - titik_p.pop(2) 
    return tinggi_dari_tanah

def main():
    
    x: int = 3
    y: int = 0
    z: int = 0

    ex: int = 4
    ey: int = -3
    ez: int = 0
    
    teta: float = 30
    
    tinggi_p: int = 100 #dalam meter

    titik = [0, x, y, z]
    sumbu_rotasi = [ex, ey, ez]

    s = Solusi(titik, sumbu_rotasi, teta)
    
    q_bar = s.convert_q_bar(s.rotasi, s.teta)
    q_conjugate = s.convert_q_conjugate(q_bar)
    v1 = s.v1_titik_hasil(s.titik_array, q_bar, q_conjugate)
    v2 = [float(round(ele, 3)) for ele in s.v2_titik_hasil(s.titik_list, q_bar)]

    # print('tipe data: ', type(v1))
    # print('tipe data: ', type(v2))

    print('\na.1. Posisi akhir P (cara manual) = ', v1)
    print('a.2. Posisi akhir P (library rotate()) = ', v2, '\n')
    print('b. ketinggian P terhadap permukaan bumi = ', cari_tinggi(v2, tinggi_p), ' meter\n')

if __name__ == '__main__':
    main()