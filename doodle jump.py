import pygame
import random

# --- AYARLAR ---
GENISLIK = 400
YUKSEKLIK = 600
HIZ = 60
YER_CEKIMI = 0.35
ZIPLAMA_GUCU = -10
PLATFORM_SAYISI = 10

# Renkler
ARKA_PLAN = (248, 248, 216) # Kağıt rengi
KARAKTER_RENK = (161, 204, 59)
PLATFORM_RENK = (60, 179, 113)
METIN_RENK = (50, 50, 50)

class Oyuncu:
    def __init__(self):
        self.genislik = 30
        self.yukseklik = 30
        self.x = GENISLIK // 2
        self.y = YUKSEKLIK - 100
        self.hiz_y = 0
        self.hiz_x = 7

    def hareket_et(self):
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT]:
            self.x -= self.hiz_x
        if tuslar[pygame.K_RIGHT]:
            self.x += self.hiz_x

        # Ekranın yanından dolanma (Teleport)
        if self.x > GENISLIK:
            self.x = -self.genislik
        elif self.x < -self.genislik:
            self.x = GENISLIK

        # Yerçekimi ve Dikey Hareket
        self.hiz_y += YER_CEKIMI
        self.y += self.hiz_y

    def ciz(self, ekran):
        pygame.draw.rect(ekran, KARAKTER_RENK, [self.x, self.y, self.genislik, self.yukseklik], 0, 5)
        # Gözler
        pygame.draw.circle(ekran, (0, 0, 0), (int(self.x + 10), int(self.y + 10)), 3)
        pygame.draw.circle(ekran, (0, 0, 0), (int(self.x + 20), int(self.y + 10)), 3)

class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.genislik = 60
        self.yukseklik = 12

    def ciz(self, ekran):
        pygame.draw.rect(ekran, PLATFORM_RENK, [self.x, self.y, self.genislik, self.yukseklik], 0, 3)

def ana_dongu():
    pygame.init()
    ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    pygame.display.set_caption("Cyberia Doodle Jump")
    saat = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24, bold=True)

    oyuncu = Oyuncu()
    # İlk platformu oyuncunun altına koyalım
    platformlar = [Platform(GENISLIK // 2 - 30, YUKSEKLIK - 50)]
    
    # Rastgele başlangıç platformları
    for i in range(PLATFORM_SAYISI):
        platformlar.append(Platform(random.randint(0, GENISLIK - 60), random.randint(0, YUKSEKLIK - 100)))

    skor = 0
    en_yuksek_skor = 0
    oyun_bitti = False

    while True:
        ekran.fill(ARKA_PLAN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and oyun_bitti:
                    # Sıfırla
                    oyuncu = Oyuncu()
                    platformlar = [Platform(GENISLIK // 2 - 30, YUKSEKLIK - 50)]
                    for i in range(PLATFORM_SAYISI):
                        platformlar.append(Platform(random.randint(0, GENISLIK - 60), random.randint(0, YUKSEKLIK - 100)))
                    skor = 0
                    oyun_bitti = False

        if not oyun_bitti:
            oyuncu.hareket_et()

            # Platform Çarpışma Kontrolü (Sadece aşağı düşerken)
            if oyuncu.hiz_y > 0:
                for p in platformlar:
                    if (oyuncu.x + oyuncu.genislik > p.x and 
                        oyuncu.x < p.x + p.genislik and 
                        oyuncu.y + oyuncu.yukseklik > p.y and 
                        oyuncu.y + oyuncu.yukseklik < p.y + p.yukseklik + oyuncu.hiz_y):
                        oyuncu.hiz_y = ZIPLAMA_GUCU
                        break

            # Ekran Kaydırma (Scrolling)
            if oyuncu.y < 200:
                kayma_miktari = abs(oyuncu.hiz_y)
                oyuncu.y += kayma_miktari
                skor += int(kayma_miktari // 10)
                for p in platformlar:
                    p.y += kayma_miktari
                    # Ekrandan çıkan platformu sil ve yukarıda yenisini oluştur
                    if p.y > YUKSEKLIK:
                        platformlar.remove(p)
                        platformlar.append(Platform(random.randint(0, GENISLIK - 60), random.randint(-50, 50)))

            # Ölüm Kontrolü
            if oyuncu.y > YUKSEKLIK:
                oyun_bitti = True
                if skor > en_yuksek_skor:
                    en_yuksek_skor = skor

        # Çizimler
        for p in platformlar:
            p.ciz(ekran)
        oyuncu.ciz(ekran)

        # Arayüz
        skor_metni = font.render(f"SKOR: {skor}", True, METIN_RENK)
        ekran.blit(skor_metni, (10, 10))

        if oyun_bitti:
            bitti_metni = font.render("OYUN BITTI!", True, (200, 0, 0))
            tekrar_metni = font.render("Tekrar: SPACE", True, METIN_RENK)
            ekran.blit(bitti_metni, (GENISLIK // 2 - 70, YUKSEKLIK // 2 - 20))
            ekran.blit(tekrar_metni, (GENISLIK // 2 - 80, YUKSEKLIK // 2 + 20))

        pygame.display.flip()
        saat.tick(HIZ)

if __name__ == "__main__":
    ana_dongu()
