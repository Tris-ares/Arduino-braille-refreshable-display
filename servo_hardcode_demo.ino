#include <Stepper.h>
//#include <Streaming.h>
int nb;

// change this to fit the number of steps per revolution for your motor
const int stepsPerRevolution = 64 * 16; //90°

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 11, 9, 8, 10);

void setup() {
  Serial.begin(9600);
  // set the speed in rpm:
  myStepper.setSpeed(20);
}

void loop() {
  char* rotation[] = {"positive", "3", "negative", "5", "positive", "6"};
  //First tour
  convert (rotation[1]);
  // step one revolution  in one direction:
  if (rotation[0] == "positive") {
    myStepper.step(nb * stepsPerRevolution);
  }
  else {
    myStepper.step(-nb * stepsPerRevolution);
  }
//Second tour
  convert (rotation[3]);
  // step one revolution  in one direction:
  if (rotation[2] == "positive") {
    myStepper.step(nb * stepsPerRevolution);
  }
  else {
    myStepper.step(-nb * stepsPerRevolution);
  }
//Final tour
  convert (rotation[5]);
  // step one revolution  in one direction:
  if (rotation[4] == "positive") {
    myStepper.step(nb * stepsPerRevolution);
  }
  else {
    myStepper.step(-nb * stepsPerRevolution);
  }
  delay(100);
}

//Test the string if it's the correct number and store it in a variable
void convert (char* toconvert) {
  if (toconvert == "0") {
    nb = 0;
  }
  if (toconvert == "1") {
    nb = 1;
  }
  else if (toconvert == "2") {
    nb = 2;
  }
  else if (toconvert == "3") {
    nb = 3;
  }
  else if (toconvert == "4") {
    nb = 4;
  }
  else if (toconvert == "5") {
    nb = 5;
  }
  else if (toconvert == "6") {
    nb = 6;
  }
  else if (toconvert == "7") {
    nb = 7;
  }
  else if (toconvert == "8") {
    nb = 8;
  }
  else if (toconvert == "9") {
    nb = 9;
  }
  else if (toconvert == "10") {
    nb = 10;
  }
}

