# Merge Mail Project

## Project Overview
This is a tool to merge names from a mailing list with a document. 


## Objectives
- Import the document file
- Import the mailing list
- Apply text formatting to the names in the mailing list
- Insert names into the document.
- Save the new documents. 

## Results
To conclude, this tool could be used to merge any list (such as names) with a document file to save time. 

## Process

```mermaid
flowchart TD
start(((START)))
letter{Get Letter Module}
mailing_list{Get Mailing List Module}
mail_merge{Merge Mail Module}
import_letter[Import Letter File]
import_mail[Import Mailing List]
apply_formatting[Apply Text Formatting]
apply_text[Apply Formatted Text From Mailing List to Document]
save[Save New Document for Delivery]
finish(((END)))
start --> letter
start --> mailing_list
letter --> import_letter
import_letter --> mail_merge
mailing_list --> import_mail
import_mail --> apply_formatting
apply_formatting --> mail_merge
mail_merge --> apply_text
apply_text --> save
save --> finish
