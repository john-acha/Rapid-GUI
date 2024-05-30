import sys
import time

from PyQt6.QtCore import Qt, QTime,  QTimer
from PyQt6.QtGui import QFont, QFontMetrics, QPainter, QPixmap, QTextDocument
from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock

while QTime.currentTime() < due:
    time.sleep(20) # 20 seconds

font = QFont("Helvetica", 36, QFont.Weight.Bold)
fm = QFontMetrics(font)
pixmap = QPixmap(fm.horizontalAdvance(message) + 5, fm.height() + 5)
pixmap.fill(Qt.GlobalColor.white)
painter = QPainter(pixmap)
document = QTextDocument()
document.setDefaultFont(font)
document.setHtml("<font color=red>{}</font>".format(message))
document.drawContents(painter)
painter.end()
label = QLabel()
label.setPixmap(pixmap)
label.setMask(pixmap.createMaskFromColor(Qt.GlobalColor.white))
label.setWindowFlags(Qt.WindowType.SplashScreen | Qt.WindowType.FramelessWindowHint)
label.show()
QTimer.singleShot(60000, app.quit) # 1 minute
sys.exit(app.exec())
