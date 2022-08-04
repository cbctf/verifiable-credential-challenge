
## Verifiable Credential Challenge

ITPSS wants to send the holder an education certificate that can be verified using the blockchain. This challenge is based on W3 Verifiable Credentials Model. (ITPSS is an issuer and also the verifier). The flag will be in the following format: CBCTF{CTF_THIS_IS_AN_EXAMPLE}.

![Alt text](./verifiablecred.png?raw=true "Title")

## Challenge 1 - Finding the Schema Name

Run ITPSS Agent in one instance and holder Agent in another instance. Connect ITPSS with the holder by copying the invitation JSON detail to the holder. Using the (3) get flag command and input the schema name. The flag will show in the holder’s terminal.

## Challenge 2 - Finding the Holder's Full Name

ITPSS now issue a credential to the holder. Using the list of command given in ITPSS terminal. Using the (3) get flag command and input the holder’s full name. The flag will show in the holder’s terminal.

## To run the agent, open two instances in Dockerplay: 
In your browser, go to the docker playground service [Play with Docker](https://labs.play-with-docker.com/). On the title screen, click "Start". On the next screen, click (in the left menu) "+Add a new instance".  That will start up a terminal in your browser. Run the following commands to start the itpss agent:

ITPSS's Instance

```bash
git clone https://github.com/haziq-hamzani/verifiable-credential-challenge
cd verifiable-credential-challenge/demo
LEDGER_URL=http://dev.greenlight.bcovrin.vonx.io ./run_demo itpss
```

Holder's Instance
```bash
git clone https://github.com/haziq-hamzani/verifiable-credential-challenge
cd verifiable-credential-challenge/demo
LEDGER_URL=http://dev.greenlight.bcovrin.vonx.io ./run_demo holder
```

