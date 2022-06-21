# Project Creator
Project Creator è un programma  CLI gratuito, per la creazione automatica di progetti. Crea quello locale, quindi lo collega al Github Remote Repo.

## Set Up
Scarica la cartella ZIP o clona il repository con:
```
git clone https://github.com/TonicStark/Project-Creator.git
```

Quindi installa le dipendenze in un virtualenv, puoi crearne uno tramite `python -m venv <name of the virtualenv>`, con:
```
pip install -r requirements.txt
```

## Personalizzazione
### Percorso dei Progetti
Devi specificare, quale è il percorso sulla tua macchina, dove _solitamente_ memorizzi tutti i tuoi progetti:
```python
PROJECTS_PATH = "D:\\GitHub"
```
### Variabili d'Ambiente
Nel file `.env` ci sono 2 variabili: **USERNAME** e **TOKEN**. Nel nome utente, devi inserire il tuo nome utente Github; nel token il tuo token di accesso a Github.

Per creare un token, [qui](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) c'è la Guida Ufficiale di Github.

**Nota**: imposta **Nessuna scadenza** per una migliore esperienza utente, usalo **SOLO** per questa automazione e concedi **SOLO i privilegi più semplici**: solo per **creare** e **aggiornare** le repository.

# Avvia lo Script
Ora che hai configurato tutte le opzioni, prova questo Script. Se hai VS Code, aprirà automaticamente anche l'editor nella cartella del progetto appena creata! **Buona Automazione!**