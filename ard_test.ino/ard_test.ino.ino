/* Sensor test sketch
  for more information see http://www.ladyada.net/make/logshield/lighttemp.html
  */
 
#define aref_voltage 2.56         

int led = 13; 
 
 
//TMP36 Pin Variables
int tempPin = 1;        //the analog pin the TMP36's Vout (sense) pin is connected to
                        //the resolution is 10 mV / degree centigrade with a
                        //500 mV offset to allow for negative temperatures
int tempReading;        // the analog reading from the sensor
 
void setup(void) {
  // We'll send debugging information via the Serial monitor
  Serial.begin(115200);   
}
 
 
void loop(void) {

int inByte;

// wait for prompt from the Python script
if (Serial.available() > 0) {

// use led 13 to show that the measure and communication is under way
    digitalWrite(led, HIGH);

      
      while (inByte != "0"){
        inByte = Serial.read();
      }
        Serial.print(inByte);
        Serial.print("\n");

      digitalWrite(led, LOW);
    

    }
}
