int en1 = 9;
int in1 = 8;
int in2 = 7;
int en2 = 3;
int in3 = 5;
int in4 = 4;
int led=6;
int value[3];
int speedA = 150;
int speedB = 150;

void setup()
{
  pinMode(en1, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(en2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(led,OUTPUT);
  //Motor A
  digitalWrite(en1, LOW);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  // Motor B
  digitalWrite(en2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  Serial.begin(9600);

}
void loop()
{
  while(Serial.available() >= 1)
  {
    for (int i = 0; i < 3; i++){
      value[i] = Serial.read();
    }
  }
  if(value[2]==1)
  {
    digitalWrite(led,HIGH);
    delay(100);
    digitalWrite(led,LOW);
  }
  if(value[2]==2)
  {
     digitalWrite(led,HIGH);
    delay(100);
    digitalWrite(led,LOW);
    delay(100);
    digitalWrite(led,HIGH);
    delay(100);
    digitalWrite(led,LOW);
  }
  speedA = speedA + value[0];
  speedB = speedB + value[1];
  analogWrite(en1, speedA);
  analogWrite(en2, speedB);
}
