#include <OSCBoards copy.h>
#include <OSCBoards.h>
#include <OSCBundle.h>
#include <OSCData.h>
#include <OSCMatch.h>
#include <OSCMessage.h>
#include <OSCTiming.h>
#include <SLIPEncodedSerial.h>
#include <SLIPEncodedUSBSerial.h>

int pot0 = A0;
int pot1 = A1;
int pot2 = A2;
int pot3 = A3;
int pot4 = A4;
int pot5 = A5;
int s0 = 2;
int s1 = 3;
int s2 = 4;
int s3 = 5;
int s4 = 6; 
int s5 = 7;
int sA = 8;

SLIPEncodedSerial SLIPSerial(Serial);

void setup() {
  //begin SLIPSerial just like Serial
  Serial.begin(9600);
}

void loop(){
  Serial.println(String(digitalRead(s0)) + "-" + String(digitalRead(s1)) + "-" + String(digitalRead(s2)) + 
                "-" +  String(digitalRead(s3)) + "-" + String(digitalRead(s4)) + "-" + String(digitalRead(s5)) + "+" 
                + String(analogRead(pot0)) + "-" + String(analogRead(pot1)) + "-" + String(analogRead(pot2)) + "-"
                + String(analogRead(pot3)) + "-" + String(analogRead(pot4)) + "-" + String(analogRead(pot5)) + "+" + String(digitalRead(sA)));
  delay(400);
}

