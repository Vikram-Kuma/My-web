const int IR0 = 2;

const int IR1 = 4;

const int IR2 = 5;

const int IR3 = 6;

const int IR4 = 7;

const int IR5 = 8;



//Motor control pins- 

//left motor- MOT0 & MOT1

//right motor- MOT2 & MOT3

const int MOT0 = 3;

const int MOT1 = 11;

const int MOT2 = 9;

const int MOT3 = 10;



void setup() {

      pinMode(MOT0,OUTPUT);

      pinMode(MOT1,OUTPUT);

      pinMode(MOT2,OUTPUT);

      pinMode(MOT3,OUTPUT);

      pinMode(IR0,INPUT);

      pinMode(IR1,INPUT);

      pinMode(IR2,INPUT);

      pinMode(IR3,INPUT);

      pinMode(IR4,INPUT);

      pinMode(IR5,INPUT);
      // initialize the serial communications:

      Serial.begin(112500);

}
void loop() {

      int S2 = digitalRead(IR0);

      int S3 = digitalRead(IR1);

      int S4 = digitalRead(IR2);

      int S5 = digitalRead(IR3);

      int S6 = digitalRead(IR4);

      int S7 = digitalRead(IR5);

      // print the sensor values:

      if (S2==1 && S3==1 && S4==0 && S5==0 && S6==1 && S7==1) {

            //follower moving towads right, stop left motor

            //digitalWrite(MOT0,LOW);

            digitalWrite(MOT0,HIGH);

            digitalWrite(MOT1,LOW);

            digitalWrite(MOT2,HIGH);

            digitalWrite(MOT3,LOW);
      }
       else if (S2==1 && S3==1 && (S4==0 || S5==0) && S6==1 && S7==1) {

            //follower moving towads right, stop left motor

            //digitalWrite(MOT0,LOW);

            digitalWrite(MOT0,HIGH);

            digitalWrite(MOT1,LOW);

            digitalWrite(MOT2,HIGH);

            digitalWrite(MOT3,LOW);
      }
      else if ((S2==0 || S3==0) && S4==0 && S5==0 && S6==1 && S7==1) {

            //follower moving towads right, stop left motor

            //digitalWrite(MOT0,LOW);

            digitalWrite(MOT0,LOW);

            analogWrite(MOT1,125);

            analogWrite(MOT2,125);

            digitalWrite(MOT3,LOW);
      }
      else if ((S2==0 || S3==0) && S4==0 && S5==1 && S6==1 && S7==1) {

            //follower moving towads right, stop left motor

            //digitalWrite(MOT0,LOW);

            digitalWrite(MOT0,LOW);

            digitalWrite(MOT1,LOW);

            digitalWrite(MOT2,HIGH);

            digitalWrite(MOT3,LOW);
      }
        else if (S2==1 && S3==1 && S4==0 && S5==0 && (S6==0 || S7==0)) {

            //follower moving towads left, stop right motor

            digitalWrite(MOT0,HIGH);

            digitalWrite(MOT1,LOW);

            digitalWrite(MOT2,LOW);

            //digitalWrite(MOT3,LOW);

            digitalWrite(MOT3,LOW);

      }
            else if (S2==0 && S3==0 && S4==0 && S5==0 && S6==0 && S7==0) {

            //stop

            digitalWrite(MOT0,LOW);

            analogWrite(MOT1,125);

            digitalWrite(MOT2,HIGH);

            digitalWrite(MOT3,LOW);

      }
       else if (S2==1 && S3==1 && S4==1 && S5==1 && S6==1 && S7==1) {

            //stop

            digitalWrite(MOT0,LOW);

            analogWrite(MOT1,125);

            digitalWrite(MOT2,HIGH);

            digitalWrite(MOT3,LOW);

      }
       else {

            //stop follower

            digitalWrite(MOT0,LOW);

            digitalWrite(MOT1,LOW);

            digitalWrite(MOT2,LOW);

            digitalWrite(MOT3,LOW);

      }
      } 
