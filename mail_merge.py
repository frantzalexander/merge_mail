from get_mail import GetMail
from get_letter import GetLetter

guest_list = "./Input/Names/invited_names.txt"
invitation_letter = "./Input/Letters/starting_letter.txt"

mailing_list = GetMail(mailing_list_filepath = guest_list)
letter = GetLetter(letter_filepath = invitation_letter)

guest_mailing_list = mailing_list.guest_list

for guest in mailing_list.guest_list:
    letter_with_guest_name = letter.contents.replace("[name]", guest)
    with open(f"./Output/ReadyToSend/invitation_letter_to_{guest}.txt", mode = "w") as invitation_letter:
        invitation_letter.write(letter_with_guest_name)