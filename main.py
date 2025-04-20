from __future__ import annotations

from pathlib import Path
import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
        
    dataList = [
            ["name", "surname", "1", "City", "Street"],
            ["name", "surname", "1", "City", "Street"]
    ]

    view = QQuickView()
    view.setInitialProperties({"model":dataList})
    view.setSource(QUrl.fromLocalFile(Path(__file__).parent/"folder"/"view.qml"))
    view.show()

    exit_code = app.exec()
    del view
    sys.exit(exit_code)

