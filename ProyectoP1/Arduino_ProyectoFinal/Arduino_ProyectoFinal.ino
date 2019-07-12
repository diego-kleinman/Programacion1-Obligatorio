int valorLDR = 0;
int pinLDR = A0;
float temp;
int pinLM35 = A1;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0,INPUT);
   
}

void loop() {
  // put your main code here, to run repeatedly:
  temp = analogRead(pinLM35)*0.26 ;
  valorLDR = analogRead(pinLDR);
  Serial.println((String)temp + "," + (String)valorLDR);
  delay(300000); //Toma datos cada 5m
  
}
