/*
 * JuanaBin-PH 🇵🇭
 * Smart Waste Segregation System
 * Solar-Ready + IoT
 * Author: JuanaBinPH Team
 */

#include <Servo.h>

const int IR_PIN = 2;
const int SERVO_PIN = 9;

Servo binServo;

void setup() {
  Serial.begin(9600);
  binServo.attach(SERVO_PIN);
  pinMode(IR_PIN, INPUT);
  binServo.write(0);
  Serial.println("JuanaBin-PH Initialized - Ready for segregation");
}

void loop() {
  int wasteDetected = digitalRead(IR_PIN);
  
  if (wasteDetected == LOW) {
    Serial.println("Waste detected!");
    // TODO: Add AI classification here
    // For now, open biodegradable bin
    binServo.write(90);
    delay(2000);
    binServo.write(0);
    delay(1000);
  }
}
filwininc@gmail.com. Press tab to insert.
