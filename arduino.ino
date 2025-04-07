#include <Servo.h>

Servo myServo;

void setup() {
    myServo.attach(5);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        int angle = command.toInt();
        if (angle >= 0 && angle <= 180)
            myServo.write(angle);
    }
}
