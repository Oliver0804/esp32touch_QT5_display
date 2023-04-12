# esp32touch_QT5_display
## esp32touch_QT5_display是一個用於Touch的數值可視化的工具，它可以協助評估觸摸情況和電容量讀取到的數值的變化。

這個工具的核心部分是一個Python腳本，它可以通過串口從ESP32開發板讀取Touch感測器的數據，然後使用PyQt5庫繪製一個包含10個長條圖的GUI界面，每個長條圖代表一個Touch通道的讀數。當Touch感測器的電容量變化時，長條圖的高度也會隨之變化，以顯示Touch感測器的讀數變化。

該工具的使用非常簡單，你只需要將ESP32開發板連接到你的計算機，然後運行Python腳本即可。工具會自動檢測可用的串口並打開它，然後從串口讀取Touch感測器的數據並顯示在GUI界面上。

這個工具可以幫助你評估Touch感測器的性能和讀數變化，並幫助你進行Touch感測器的校準和優化。它對於開發和測試Touch感測器應用程序非常有用，也可以用於教學和學習。

## esp32 代碼
可參照官方idf 5.0版本
https://github.com/espressif/esp-idf/tree/master/examples/peripherals/touch_sensor/touch_sensor_v1/touch_pad_read

![iamge](https://github.com/Oliver0804/esp32touch_QT5_display/blob/main/%E6%88%AA%E5%9C%96%202023-04-12%20%E4%B8%8B%E5%8D%881.44.57.png)
![iamge](https://github.com/Oliver0804/esp32touch_QT5_display/blob/main/%E6%88%AA%E5%9C%96%202023-04-12%20%E4%B8%8B%E5%8D%881.45.25.png)

https://youtube.com/shorts/AjMWdhzhyFI
