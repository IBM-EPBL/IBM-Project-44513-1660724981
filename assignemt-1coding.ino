int trigger_pin = 2;
int echo_pin = 3;
int buzzer_pin = 10;
int time;
int distance;
void setup()
{
        Serial.begin(9600);
        pinMode(A0,INPUT);
        pinMode(13,OUTPUT);
        pinMode(trigger_pin,OUTPUT);
 	    pinMode(echo_pin,INPUT);
        pinMode(buzzer_pin,OUTPUT);
}
void loop()
{
  double a = analogRead(A0);
  int temp = (((a/1024)*5)-0.5)*100;
  Serial.println(temp);
  if(temp>100)
    digitalWrite(13,HIGH);
  else
    digitalWrite(13,LOW);
  delay(1000);
  digitalWrite(trigger_pin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger_pin,LOW);
  time = pulseIn(echo_pin,HIGH);
  distance = (time*0.034)/2;
  if(distance<=10)
  {
    Serial.println("Door Open");
    Serial.print("Distance=");
    Serial.println(distance);
    digitalWrite(buzzer_pin,HIGH);
    delay(500);
  }
  else
  {
    Serial.println("Door Open");
    Serial.print("Distance=");
    Serial.println(distance);
    digitalWrite(buzzer_pin,LOW);
    delay(500);
  }
}
  
  
  
