import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import serial

class SerialReader(QThread):
    data_parsed = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        # Configure serial port
        ser = serial.Serial('/dev/tty.usbserial-1442401', baudrate=115200)

        while True:
            # Read and parse data
            line = ser.readline().decode('utf-8').strip()
            data = re.findall(r'T\d+:\[\s*(\d+),\s*\d+\]', line)

            if len(data) == 10:
                parsed_data = {f'T{i}': int(value) for i, value in enumerate(data)}
                self.data_parsed.emit(parsed_data)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('T0-T9 Bar Chart')

        # Set up chart
        self.series = QBarSeries()

        self.bar_set = QBarSet('')
        self.bar_set.append([0] * 10)
        self.series.append(self.bar_set)

        self.chart = QChart()
        self.chart.addSeries(self.series)

        self.categories = ['T{}'.format(i) for i in range(10)]
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 1200)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.chart.legend().setVisible(False)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set up layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.chart_view)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()

        # Start reading data
        self.serial_reader = SerialReader()
        self.serial_reader.data_parsed.connect(self.update_chart)
        self.serial_reader.start()

    def update_chart(self, parsed_data):
        for i, value in parsed_data.items():
            index = int(i[1])
            self.bar_set.replace(index, value)

        self.chart_view.update()

        # Print parsed data
        print(parsed_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
