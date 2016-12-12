#include <OSCBoards copy.h>
#include <OSCBoards.h>
#include <OSCBundle.h>
#include <OSCData.h>
#include <OSCMatch.h>
#include <OSCMessage.h>
#include <OSCTiming.h>
#include <SLIPEncodedSerial.h>
#include <SLIPEncodedUSBSerial.h>

int pot = A1;
int s1 = 7;

SLIPEncodedSerial SLIPSerial(Serial);

void setup() {
  //begin SLIPSerial just like Serial
  Serial.begin(9600);
}

int i = 1;
void loop(){
  if (i > 1000) {
    i = 0;
  }
  Serial.println(String(digitalRead(s1)) + "-" + String(analogRead(pot)) + "-" + String(i));
  i++;
  delay(200);
}

