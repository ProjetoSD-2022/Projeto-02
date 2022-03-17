const int allPins[] = {13, 12, 11, 10};
const int geladeiraPin = allPins[0];
const int fogaoPin = allPins[1];
const int ventPin = allPins[2];
const int tvPin = allPins[3];
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(geladeiraPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();

    // Comando liga-desliga para geladeira (G para on e g para off)
    if (incomingByte == 'G' | incomingByte == 'g'){
      acende_desliga(incomingByte, geladeiraPin);
    }

    // Comando liga-desliga para fogao (F para on e f para off)
    if (incomingByte == 'F' | incomingByte == 'f'){
      acende_desliga(incomingByte, fogaoPin);
    }

    // Comando liga-desliga para ventilador (V para on e v para off)
    if (incomingByte == 'V' | incomingByte == 'v'){
      acende_desliga(incomingByte, ventPin);
    }

    // Comando liga-desliga para TV (T para on e t para off)
    if (incomingByte == 'T' | incomingByte == 't'){
      acende_desliga(incomingByte, tvPin);
    }

    if (incomingByte == 'H' | incomingByte == 'l'){
      for (int i = 0; i < sizeof(allPins)/sizeof(int); i++){
        acende_desliga(incomingByte, allPins[i]);
      }
    }
  }
}

void acende_desliga(int comando, const int pin){
  if (isUpperCase(comando) == true){
    digitalWrite(pin, HIGH);
  }
  else{
    digitalWrite(pin, LOW);
  }
}
