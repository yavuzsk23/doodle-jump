# Doodle Jump (Python Edition)

A lightweight Doodle Jump clone built with Python and Pygame — endless platform jumping with screen wrapping, camera scrolling, and a simple scoring system.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Pygame](https://img.shields.io/badge/Pygame-2.x-green)

---

## 🇬🇧 English

### About
This is a small recreation of the classic Doodle Jump, made as a way to practice core 2D game mechanics in Pygame: gravity, jump physics, camera scrolling, and procedural platform generation. The character automatically jumps whenever it lands on a platform while falling — the only thing you control is left/right movement.

### Features
- Automatic jumping on platform contact (no jump button needed, just like the original)
- Screen-wrap movement — walk off one edge, appear on the other
- Camera scrolling that follows the player upward, with platforms recycling as they scroll off-screen
- Score based on height climbed
- Game over when you fall off the bottom of the screen, with instant retry

### Controls
| Key | Action |
|---|---|
| `←` `→` | Move left / right |
| `Space` | Retry after game over |

### Installation & Running
```bash
pip install pygame
python doodle_jump.py
```

### Requirements
- Python 3.8+
- Pygame

### How It Works
The player only falls or jumps — there's no manual jump input. Gravity constantly pulls the player down, and colliding with a platform while falling triggers an automatic upward bounce. Once the player climbs above a certain height on screen, everything scrolls downward instead — platforms, background, and score update together to create the illusion of endless upward movement. Platforms that scroll off the bottom of the screen are removed and respawned near the top, keeping the level infinite without ever storing more than `PLATFORM_COUNT` platforms in memory.

### Possible Improvements
- Moving/breakable platform types
- Power-ups (springs, jetpacks, shields)
- Persistent high score (saved to a file)
- Sound effects and background music

---

## 🇩🇪 Deutsch

### Über das Projekt
Dies ist eine kleine Nachbildung des klassischen Doodle Jump, entstanden zum Üben grundlegender 2D-Spielmechaniken in Pygame: Schwerkraft, Sprungphysik, Kamera-Scrolling und prozedurale Plattformerzeugung. Der Charakter springt automatisch, sobald er beim Fallen auf einer Plattform landet — gesteuert wird nur die Links-/Rechtsbewegung.

### Funktionen
- Automatisches Springen bei Plattformkontakt (kein Sprungtaste nötig, genau wie im Original)
- Bildschirm-Wrap — läuft man an einem Rand hinaus, erscheint man am anderen wieder
- Kamera-Scrolling, das dem Spieler nach oben folgt, wobei Plattformen beim Verlassen des Bildschirms wiederverwendet werden
- Punktestand basierend auf der erreichten Höhe
- Game Over beim Herunterfallen vom Bildschirm, mit sofortigem Neustart

### Steuerung
| Taste | Aktion |
|---|---|
| `←` `→` | Nach links / rechts bewegen |
| `Leertaste` | Neustart nach Game Over |

### Installation und Ausführung
```bash
pip install pygame
python doodle_jump.py
```

### Voraussetzungen
- Python 3.8+
- Pygame

### Funktionsweise
Der Spieler fällt oder springt nur — es gibt keine manuelle Sprungeingabe. Die Schwerkraft zieht den Spieler ständig nach unten, und eine Kollision mit einer Plattform während des Fallens löst einen automatischen Sprung nach oben aus. Sobald der Spieler eine bestimmte Höhe auf dem Bildschirm erreicht, scrollt stattdessen alles nach unten — Plattformen, Hintergrund und Punktestand werden gemeinsam aktualisiert, um die Illusion einer endlosen Aufwärtsbewegung zu erzeugen. Plattformen, die unten aus dem Bildschirm scrollen, werden entfernt und oben neu erzeugt, wodurch das Level unendlich bleibt, ohne jemals mehr als `PLATFORM_COUNT` Plattformen im Speicher zu halten.

### Mögliche Erweiterungen
- Bewegliche/zerbrechliche Plattformtypen
- Power-ups (Sprungfedern, Jetpacks, Schilde)
- Dauerhafter Highscore (in Datei gespeichert)
- Soundeffekte und Hintergrundmusik

---

## 🇹🇷 Türkçe

### Proje Hakkında
Bu, klasik Doodle Jump'ın Pygame'de temel 2D oyun mekaniklerini (yer çekimi, zıplama fiziği, kamera kaydırma, rastgele platform üretimi) pratik etmek amacıyla yapılmış küçük bir versiyonu. Karakter, düşerken bir platforma her temas ettiğinde otomatik olarak zıplıyor — senin kontrol ettiğin tek şey sağa/sola hareket.

### Özellikler
- Platforma değince otomatik zıplama (orijinalinde olduğu gibi ayrı bir zıplama tuşu yok)
- Ekran kenarından çıkınca diğer kenardan geri gelme (screen wrap)
- Oyuncuyu yukarı doğru takip eden kamera kaydırması; ekrandan çıkan platformlar geri kullanılıyor
- Çıkılan yüksekliğe göre skor hesaplama
- Ekranın altından düşünce oyun bitiyor, anında yeniden deneme imkanı

### Kontroller
| Tuş | İşlev |
|---|---|
| `←` `→` | Sağa / sola hareket |
| `Boşluk` | Oyun bitince yeniden başla |

### Kurulum ve Çalıştırma
```bash
pip install pygame
python doodle_jump.py
```

### Gereksinimler
- Python 3.8+
- Pygame

### Nasıl Çalışır
Oyuncu sadece düşer ya da zıplar — elle zıplama girdisi yok. Yer çekimi oyuncuyu sürekli aşağı çekiyor, düşerken bir platforma çarpınca otomatik olarak yukarı fırlatılıyor. Oyuncu ekranda belirli bir yüksekliğin üzerine çıkınca bu sefer her şey aşağı kayıyor — platformlar, arka plan ve skor birlikte güncellenerek sonsuz yukarı hareket illüzyonu yaratılıyor. Ekranın altından kayıp giden platformlar kaldırılıp üstte yeniden oluşturuluyor, bu sayede bellekte hiçbir zaman `PLATFORM_COUNT`'tan fazla platform tutulmadan seviye sonsuz kalıyor.

### Geliştirilebilecek Noktalar
- Hareketli/kırılabilir platform türleri
- Güçlendirmeler (yaylar, jetpack, kalkan)
- Kalıcı en yüksek skor (dosyaya kaydedilen)
- Ses efektleri ve arka plan müziği

---

**Author:** Yavuz
