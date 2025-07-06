#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <HardwareSerial.h>
#include <UniversalTelegramBot.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* botToken = "your_BOT_TOKEN";
const char* chatID = "your_CHAT_ID";

HardwareSerial serialGPS(1);
WiFiClientSecure secured_client;
UniversalTelegramBot bot(botToken, secured_client);

String getGPSData() {
  String data = "";
  while (serialGPS.available()) {
    data += char(serialGPS.read());
  }
  return data;
}

void setup() {
  Serial.begin(115200);
  serialGPS.begin(9600, SERIAL_8N1, 16, 17); // RX = 16, TX = 17
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
  secured_client.setInsecure();
}

void loop() {
  String gpsData = getGPSData();
  if (gpsData.length() > 0) {
    bot.sendMessage(chatID, "GPS Data: " + gpsData, "");
    Serial.println("Sent: " + gpsData);
  }
  delay(10000);
}
