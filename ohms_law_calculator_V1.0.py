# Ohm's Law calculator Project
# This program calculates voltage, current, resistance, and power using Ohm's Law.
# Ohm's law states that V = I * R, Where V is voltage (in volts), I is current (In amps), and R is resistance (in ohms).
# The program also calculates power using the formula P = V * I, where P is power (in watts).

#Welcome message
print("Welcome to the ohm's law calculator!")
print("This program calculates voltage, current, resistance, and power using Ohm's Law.")

# Instructions

# Fill in data
print("Please introduce the values you know:")
print("If you don't know the value, just press enter.")
values_count = 0
while values_count <2:
    voltage = input("Voltage (V): ").strip()
    current = input("Current (I): ").strip()
    resistance = input("Resistance (R): ").strip()
    power = input("Power (P): ").strip()
    values = [voltage, current, resistance, power]

    #Check if the user has entered at least two values
    
    values_count = sum(1 for value in values if value !="")
    if values_count < 2:
        print("Please enter at least two values!!!") #Keep asking for values
print("...")
print("...")
print("...")
print("WONDERFUL, You have entered enough values.")
print("...")
print("...")
print("...")
# Convert the values to float
#voltage
if voltage != "":
    voltage = float(voltage)
else:
    voltage = None
#current
if current != "":
    current = float(current)
else:
    current = None
#resistance
if resistance != "":
    resistance = float(resistance)
else:
    resistance = None
#Power
if power != "":
    power = float(power)
else:
    power = None
#Printing values
print("You have entered the following values: ")
if voltage is not None:   
    print("Voltage (V): ", voltage, "V")
else:
    print("Voltage (V): ","To be calculated")
if current is not None:
    print("Current (I): ", current, "A")
else:
    print("Current (I): ","To be calculated")
if resistance is not None:
    print("Resistance (R): ", resistance, "Ohm")
else:
    print("Resistance (R): ","To be calculated")
if power is not None:
    print("Power (P): ", power, "W")
else:
    print("Power (P): ","To be calculated")

#Proceed with calculation
print("Proceeding with calculation...")
print("...")
print("...")
print("...")
print("The calculation is done.")
print("...")
print("The results are as follows:")

#Calculating the missing values
#Voltage
if voltage is None and current is not None and resistance is not None:
    voltage = current * resistance
    print("Voltage (V): ", voltage, "V")
elif voltage is None and power is not None and current is not None:
    voltage = power / current
    print("Voltage (V): ", voltage, "V")
elif voltage is None and power is not None and resistance is not None:
    voltage  =(power * resistance) ** 0.5
    print("Voltage (V): ", voltage, "V")
elif voltage is not None:
    print("Voltage (V): ", voltage, "V")
#Current
if current is None and voltage is not None and resistance is not None:
    current = voltage / resistance
    print("Current (I): ", current, "A")
elif current is None and power is not None and voltage is not None:
    current = power/voltage
    print("Current (I): ", current, "A")
elif current is None and power is not None and resistance is not None:
    current = (power / resistance) ** 0.5
    print("Current (I): ", current, "A")
elif current is not None:
    print("Current (I): ", current, "A")
#Resistance
if resistance is None and voltage is not None and current is not None:
    resistance = voltage / current
    print("Resistance (R): ", resistance, "Ohm")
elif resistance is None and power is not None and voltage is not None:
    resistance = (voltage **2) / power
    print("Resistance (R): ", resistance, "Ohm")
elif resistance is None and power is not None and current is not None:
    resistance = power / (current ** 2)
    print("Resistance (R): ", resistance, "Ohm")
elif resistance is not None:
    print("Resistance (R): ", resistance, "Ohm")
#Power
if power is None and voltage is not None and current is not None:
    power = voltage * current
    print("Power (P): ", power, "W")
elif power is None and voltage is not None and resistance is not None:
    power = (voltage ** 2) / resistance
    print("Power (P): ", power, "W")
elif power is None and current is not None and resistance is not None:
    power = (current ** 2) * resistance
    print("Power (P): ", power, "W")
elif power is not None:
    print("Power (P): ", power, "W")
#End of program