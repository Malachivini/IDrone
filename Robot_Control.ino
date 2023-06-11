#include <iostream>


// ---------------------------------------------------------------- //

// ---------------------------------------------------------------- //
//#include "NewPing.h"
#include <Stepper.h>
#include "BluetoothSerial.h"

const char *pin = "1234"; // Change this to more secure PIN.

String device_name = "ESP32-BT-roi1";


#define  echoPinL 17 // attach pin D2 Arduino to pin Echo of HC-SR04
#define  trigPinL 16 //attach pin D3 Arduino to pin Trig of HC-SR04
#define  echoPinR 4 // attach pin D2 Arduino to pin Echo of HC-SR04
#define  trigPinR 2 //attach pin D3 Arduino to pin Trig of HC-SR04
#define  echoPinF 18 // attach pin D2 Arduino to pin Echo of HC-SR04
#define  trigPinF 5 //attach pin D3 Arduino to pin Trig of HC-SR04
const int stepsPerRevolution = 1024;  // change this to fit the number of steps per revolution


// ULN2003 Motor Driver Pins
#define IN11 12
#define IN12 14
#define IN13 27
#define IN14 26
#define IN21 25
#define IN22 33
#define IN23 19
#define IN24 21

int D_R = 15;
int D_Micro=10;


// initialize the stepper library
Stepper myStepper1(stepsPerRevolution, IN11, IN13, IN12, IN14);
Stepper myStepper2(stepsPerRevolution, IN21, IN23, IN22, IN24);


// defines variables
long durationL; // variable for the duration of sound wave travel
int distanceL; // variable for the distance measurement
long durationR; // variable for the duration of sound wave travel
int distanceR; // variable for the distance measurement
long durationF; // variable for the duration of sound wave travel
int distanceF; // variable for the distance measurement

//int e = 0;
//int v = 0;
//const int N = 4;
//int* input;
//static int Distance[4] = { 0, 1, 2, 3 };
int counter_1;
static int Memory[300];
int num_Memory = 0;
int flag = 0;

BluetoothSerial SerialBT;


void setup() {
	pinMode(trigPinL, OUTPUT); // Sets the trigPin as an OUTPUT
	pinMode(echoPinL, INPUT); // Sets the echoPin as an INPUT
	pinMode(trigPinR, OUTPUT); // Sets the trigPin as an OUTPUT
	pinMode(echoPinR, INPUT); // Sets the echoPin as an INPUT
	pinMode(trigPinF, OUTPUT); // Sets the trigPin as an OUTPUT
	pinMode(echoPinF, INPUT); // Sets the echoPin as an INPUT 
	myStepper1.setSpeed(30);
	myStepper2.setSpeed(30);

	Serial.begin(115200); // // Serial Communication is starting with 9600 of baudrate speed
  SerialBT.begin(device_name); //Bluetooth device name
  Serial.printf("The device with name \"%s\" is started.\nNow you can pair it with Bluetooth!\n", device_name.c_str());
  //Serial.printf("The device with name \"%s\" and MAC address %s is started.\nNow you can pair it with Bluetooth!\n", device_name.c_str(), SerialBT.getMacString()); // Use this after the MAC method is implemented
  #ifdef USE_PIN
    SerialBT.setPin(pin);
    Serial.println("Using PIN");
  #endif

}

//void loop() {
//	measure();
//	// step one revolution in one direction:
//	//Serial.println("clockwise");
//	driveF(3, 1);
//	//driveF(2,-1);
//}

void saveBT(int num1,int num2, int num3, int num4){
  String result = String(num1) + ", " + String(num2) + ", " + String(num3) + ", " + String(num4);
  SerialBT.println(result);
}

/*void driveF(int CN, int D) {

	for (int i = 0; i < CN; i++) {
		float step1Pos = 0.0;
		float step2Pos = 0.0;

		for (int i = 0; i < stepsPerRevolution; i++)
		{
			myStepper1.step(D * 1);
			myStepper2.step(D * 1);

			// Move stepper 1 to step1Pos
			// Move stepper 2 to step2Pos
		}

	}
}*/

void driveF() {
	int CN = 1;
  saveBT(distanceR,distanceL,distanceF,0);
	for (int i = 0; i < CN; i++) {
		float step1Pos = 0.0;
		float step2Pos = 0.0;

		for (int i = 0; i < stepsPerRevolution; i++) {
			myStepper1.step(1);
			myStepper2.step(1);

		}
	}
}

void TurnLeft() {
	const int stepsPerDegree = 4; // Adjust this value for the appropriate number of steps per degree
	const int degreesToTurn = 90;
	int stepsToTurn = degreesToTurn * stepsPerDegree;
  saveBT(distanceR,distanceL,distanceF,3);

	// Rotate stepper motor to turn the car 90 degrees
	for (int i = 0; i < stepsToTurn; i++) {
		myStepper1.step(6); // Move one step in the desired direction
		//myStepper2.step(1);
		delay(10); // Add a delay between steps for smoother motion
    
	}
}

void TurnRight() {
	const int stepsPerDegree = 4; // Adjust this value for the appropriate number of steps per degree
	const int degreesToTurn = 90;
	int stepsToTurn = degreesToTurn * stepsPerDegree;
  saveBT(distanceR,distanceL,distanceF,2);

	// Rotate stepper motor to turn the car 90 degrees
	for (int i = 0; i < stepsToTurn; i++) {
		//myStepper1.step(5.85); // Move one step in the desired direction
		myStepper2.step(6);
		delay(10); // Add a delay between steps for smoother motion
	}
}


void measure() {
	// Clears the trigPin condition
	digitalWrite(trigPinL, LOW);
	delayMicroseconds(D_Micro);
	// Sets the trigPin HIGH (ACTIVE) for 10 microseconds
	digitalWrite(trigPinL, HIGH);
	delay(D_R);
	digitalWrite(trigPinL, LOW);
	// Reads the echoPin, returns the sound wave travel time in microseconds
	durationL = pulseIn(echoPinL, HIGH);
	// Calculating the distance
	distanceL = durationL * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
	// Displays the distance on the Serial Monitor
	Serial.print("SensorL Value: ");
	Serial.println(distanceL);
	/* Serial.println(" cm");



   if(13>distance||24<distance)
   {
	   Serial.println(1);
	} else if(13<distance<24)
   {
	   Serial.println(0);
	}*/

	// Clears the trigPin condition
	digitalWrite(trigPinR, LOW);
	delayMicroseconds(D_Micro);
	// Sets the trigPin HIGH (ACTIVE) for 10 microseconds
	digitalWrite(trigPinR, HIGH);
	delay(D_R);
	digitalWrite(trigPinR, LOW);
	// Reads the echoPin, returns the sound wave travel time in microseconds
	durationR = pulseIn(echoPinR, HIGH);
	// Calculating the distance
	distanceR = durationR * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
	// Displays the distance on the Serial Monitor
	Serial.print("SensorR Value: ");
	Serial.println(distanceR);



	// Clears the trigPin condition
	digitalWrite(trigPinF, LOW);
	delayMicroseconds(D_Micro);
	// Sets the trigPin HIGH (ACTIVE) for 10 microseconds
	digitalWrite(trigPinF, HIGH);
	delay(D_R);
	digitalWrite(trigPinF, LOW);
	// Reads the echoPin, returns the sound wave travel time in microseconds
	durationF = pulseIn(echoPinF, HIGH);
	// Calculating the distance
	distanceF = durationF * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
	// Displays the distance on the Serial Monitor
	Serial.print("SensorF Value: ");
	Serial.println(distanceF);
}











// Function declaration

//void turn_right();
//void turn_left();
void go_back();

//void driveF();


void loop()
{

	//input = InputElla();

	//GalgalMarcuse(input[0]);

	//MapWinitsky(input);
  delay(5000);

	while (true)
	{
		measure();
		// There is a right turn
		if (distanceR > 30)
		{
			counter_1 = 0;
			driveF();
      driveF();
      driveF();
      driveF();
			TurnRight();
			driveF();
			driveF();
			measure();
			//If we are in the room (check on the right)
			if (distanceR > 20 || distanceL > 20)
			{
				//Enter the room up to the wall
				while (distanceF > 20)
				{
					driveF();
					counter_1 += 1;
					measure();
				}
				//At the wall you will turn around and move back
				TurnLeft();
				TurnLeft();
				for (int i = 0; i < (counter_1 + 2); i++)
				{
					driveF();
				}
				TurnRight();
			}
			//If I turned to the right and it was not a room but a corridor we will continue in the loop
		}
		// There is a left turn
		else if (distanceL > 20)
		{
			counter_1 = 0;
			driveF();
      driveF();
      driveF();
      driveF();
			TurnLeft();
			driveF();
			driveF();
			measure();
			//If we are in the room (check on the right)
			if (distanceR > 20 || distanceL > 20)
			{
				//Enter the room up to the wall
				while (distanceF > 20)
				{
					driveF();
					counter_1 += 1;
					measure();
				}
				//At the wall you will turn around and move back
				TurnRight();
				TurnRight();
				for (int i = 0; i < (counter_1 + 2); i++) {
					driveF();
				}
				TurnLeft();
			}
			//If I turned to the right and it was not a room but a corridor we will continue in the loop
		}
		//If we go straight
		else if (distanceR < 20 && distanceL < 20 && distanceF > 20)
		{
			driveF();
			measure();
		}

		else if (distanceR < 20 && distanceL < 20 && distanceF < 20)
		{
			while(1){}
		}

		// Other main function logic
		// ...
	}
	//go_back();
}

