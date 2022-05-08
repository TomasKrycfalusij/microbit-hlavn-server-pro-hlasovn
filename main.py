# ÚVOD
# 1. Zmáčknutí A/B/dotykového tlačítka/pinu 2 se odešle hlas
# 2. Pinem 0 se nastaví přijímání hlasů
# 3. Pinem 1 se snažou všechny hlasy
# 4. V konzoli to vypíše váš aktuální hlas a sériové číslo microbitu
# 5. Vypíše všechny vaše předešlé hlasy (budou uloženy v listu)
# 6. Samotné čísílko mezi hlasy určuje o kolikátou pozici v listu hlasů se jedná
# 7. Nepřišel jsem na způsob jak na detekci sériového čísla v listu,
#    přesněji pozice a jak funduje přiřazování v takovém stylu listu, proto je program nedokončený
# 8. UPOZORNĚNÍ - Horní microbit je ten hlasovací, proto je možné, že ikdyž deaktivujete hlasování
#    na jednom, druhý bude stále moci přijímat hlasy. Proto pro odesílání hlasu používejte "horní"
#    a ten spodní jako "serverový" pro lepší orientaci. Pro smazání hlasů použijte serverový (spodní) microbit

radio.set_group(69)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
my_serial = control.device_serial_number()

#PROMĚNNÉ
name = "vote"
name = "send"
number = 1
value = 0
posuvnik_1 = 1
receive_message = True
list_of_votes = [{"serial": my_serial, "volba": 0}]

#Smazání dosavadních hlasů
def smazani_hlasu():
    global list_of_votes, posuvnik_1
    list_of_votes = [{"serial": my_serial, "volba": 0}]
    basic.show_icon(IconNames.TARGET)
    print("Hlasy byly smazány")
    basic.clear_screen()
    posuvnik_1 = 1
input.on_pin_pressed(TouchPin.P1, smazani_hlasu)



#ZAPNUTÍ A VYPNUTÍ MOŽNOSTI HLASOVAT
def zapinani_hlasovani():
    global receive_message
    if receive_message == True:
        global receive_message
        receive_message = False
        basic.show_icon(IconNames.NO)
    else:
        global receive_message
        receive_message = True
        basic.show_icon(IconNames.YES)
    basic.pause(500)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P0, zapinani_hlasovani)

#HLASOVANI CISEL
def voting_A():
    voted(0)
    basic.show_string("A")
    basic.clear_screen()
input.on_button_pressed(Button.A, voting_A)
def voting_B():
    voted(1)
    basic.show_string("B")
    basic.clear_screen()
input.on_button_pressed(Button.B, voting_B)
def voting_C():
    voted(2)
    basic.show_string("C")
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, voting_C)
def voting_D():
    voted(3)
    basic.show_string("D")
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P2, voting_D)
#----------------------------------------------

#ODESLÁNÍ HLASU
def voted(data):
    global list_of_votes
    radio.send_value(str(my_serial), data)

#PŘIJMUTÍ HLASU
def on_received_value(name, value):
    global list_of_votes, posuvnik_1
    if receive_message == True:
        basic.show_number(value)
        list_of_votes.append([{"serial": int(name), "volba": value}][0])
        print("Toto byl poslední přijatý hlas")
        print([{"serial": int(name), "volba": value}][0])
        posuvnik_2 = 0
        print("Toto je list tvých minulých hlasů")
        for i in range(posuvnik_1):
            print(posuvnik_2)
            print(list_of_votes[posuvnik_2])
            posuvnik_2 += 1
        posuvnik_1 += 1
        basic.pause(500)
        basic.clear_screen()
radio.on_received_value(on_received_value)