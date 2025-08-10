#!/usr/bin/env python3
# Micheal Quentin
# 01. July 2025
# Card Maintainer

import json
import os
import time
import readline

# Paths
cards_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "OITD_cards.json")

# Constants
FIELDS = ["title", "url", "image", "description", "date", "location", "setting", "identity", "time", "accommodations", "vibe"]
CARD_TITLES = []

# Completers
def field_completer(text, state):
    options = [f for f in FIELDS if f.startswith(text)]
    return options[state] if state < len(options) else None

def title_completer(text, state):
    options = [t for t in CARD_TITLES if t.lower().startswith(text.lower())]
    return options[state] if state < len(options) else None

# Custom JSON save formatting
def save_custom_format(data, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("[\n")
        for idx, card in enumerate(data):
            f.write("  {\n")
            fields = []
            if "title" in card:
                fields.append(f'    "title": "{card["title"]}"')
            if "url" in card and card["url"]:
                fields.append(f'    "url": "{card["url"]}"')
            if "image" in card and card["image"]:
                fields.append(f'    "image": "{card["image"]}"')
            if "description" in card and card["description"]:
                fields.append(f'    "description": "{card["description"]}"')
            if "date" in card and card["date"]:
                fields.append(f'    "date": "{card["date"]}"')
            if "location" in card and card["location"]:
                fields.append(f'    "location": {json.dumps(card["location"], ensure_ascii=False)}')
            if "setting" in card and card["setting"]:
                fields.append(f'    "setting": {json.dumps(card["setting"], ensure_ascii=False)}')
            if "identity" in card and card["identity"]:
                fields.append(f'    "identity": {json.dumps(card["identity"], ensure_ascii=False)}')
            if "time" in card and card["time"]:
                fields.append(f'    "time": {json.dumps(card["time"], ensure_ascii=False)}')
            if "accommodations" in card and card["accommodations"]:
                fields.append(f'    "accommodations": {json.dumps(card["accommodations"], ensure_ascii=False)}')
            if "vibe" in card and card["vibe"]:
                fields.append(f'    "vibe": {json.dumps(card["vibe"], ensure_ascii=False)}')
            f.write(",\n".join(fields))
            f.write("\n  }")
            if idx < len(data) - 1:
                f.write(",\n")
            else:
                f.write("\n")
        f.write("]\n")

while True:
    print('0: Add Card')
    print('1: Edit Card')
    print('2: Delete Card')
    selection = input('Select an option: ')

    with open(cards_json, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Refresh card titles every time
    CARD_TITLES = [card.get("title", "") for card in data if "title" in card]

    if selection == '0':
        # Add Card
        card_code = input('\nCode: ').strip()

        if card_code:
            parts = [p.strip() for p in card_code.split('|')]
            while len(parts) < 11:
                parts.append("")
            new_card = {}
            if parts[0]: new_card["title"] = parts[0]
            if parts[1]: new_card["url"] = parts[1]
            if parts[2]: new_card["image"] = parts[2]
            if parts[3]: new_card["description"] = parts[3]
            if parts[4]: new_card["date"] = parts[4]
            if parts[5]: new_card["location"] = [x.strip() for x in parts[5].split(';') if x.strip()]
            if parts[6]: new_card["setting"] = [x.strip() for x in parts[6].split(';') if x.strip()]
            if parts[7]: new_card["identity"] = [x.strip() for x in parts[7].split(';') if x.strip()]
            if parts[8]: new_card["time"] = [x.strip() for x in parts[8].split(';') if x.strip()]
            if parts[9]: new_card["accommodations"] = [x.strip() for x in parts[9].split(';') if x.strip()]
            if parts[10]: new_card["vibe"] = [x.strip() for x in parts[10].split(';') if x.strip()]
        else:
            card_title = input('Title: ').strip()
            card_url = input('URL: ').strip()
            card_image = input('Image: ').strip()
            card_description = input('Description: ').strip()
            card_date = input('Date: ').strip()
            card_location = [s.strip() for s in input('Location: ').split(';') if s.strip()]
            card_setting = [s.strip() for s in input('Setting: ').split(';') if s.strip()]
            card_identity = [s.strip() for s in input('Identity: ').split(';') if s.strip()]
            card_time = [s.strip() for s in input('Time: ').split(';') if s.strip()]
            card_accommodations = [s.strip() for s in input('Accommodations: ').split(';') if s.strip()]
            card_vibe = [s.strip() for s in input('Vibe: ').split(';') if s.strip()]

            new_card = {}
            if card_title: new_card["title"] = card_title
            if card_url: new_card["url"] = card_url
            if card_image: new_card["image"] = card_image
            if card_description: new_card["description"] = card_description
            if card_date: new_card["date"] = card_date
            if card_location: new_card["location"] = card_location
            if card_setting: new_card["setting"] = card_setting
            if card_identity: new_card["identity"] = card_identity
            if card_time: new_card["time"] = card_time
            if card_accommodations: new_card["accommodations"] = card_accommodations
            if card_vibe: new_card["vibe"] = card_vibe

        data.append(new_card)
        save_custom_format(data, cards_json)
        print(new_card.get("title","[No title]"), 'added to cards.\n')
        time.sleep(2)

    elif selection == '1':
        # Edit Card
        readline.set_completer(title_completer)
        readline.parse_and_bind("tab: complete")

        card_name = input("\nEnter the title of the card to edit: ").strip()
        matches = [c for c in data if c.get("title", "").lower() == card_name.lower()]
        if not matches:
            print("Card not found.\n")
            continue
        card = matches[0]

        readline.set_completer(field_completer)
        field = input("Field to edit: ").strip()
        if field not in FIELDS:
            print("Invalid field.\n")
            continue

        current_value = card.get(field, "")
        if isinstance(current_value, list):
            current_str = "  ;  ".join(current_value)
        else:
            current_str = current_value

        def prefill_input(prompt, text):
            def hook():
                readline.insert_text(text)
                readline.redisplay()
            readline.set_pre_input_hook(hook)
            try:
                return input(prompt)
            finally:
                readline.set_pre_input_hook()

        edit_input = prefill_input(f"Edit Field [{field}]: ", current_str).strip()

        if edit_input == "":
            if field in card:
                del card[field]
                print(f"{field} removed.")
        else:
            if field in ["location", "setting", "identity", "time", "accommodations", "vibe"]:
                new_value = [s.strip() for s in edit_input.split(';') if s.strip()]
                card[field] = new_value
            else:
                card[field] = edit_input

        save_custom_format(data, cards_json)
        print("Card updated.\n")
        time.sleep(2)

        # Reset completer
        readline.set_completer(None)

    elif selection == '2':
        # Delete Card
        readline.set_completer(title_completer)
        readline.parse_and_bind("tab: complete")

        card_name = input("\nEnter the title of the card to delete: ").strip()
        data = [c for c in data if c.get("title", "").lower() != card_name.lower()]
        save_custom_format(data, cards_json)
        print(card_name, "deleted.\n")
        time.sleep(2)

        # Reset completer
        readline.set_completer(None)

    elif selection == '':
        # Exit the program
        exit()
