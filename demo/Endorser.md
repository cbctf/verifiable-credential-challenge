# Endorser Demo

There are two ways to run the holder/itpss demo with endorser support enabled.


## Run itpss as an Author, with a dedicated Endorser agent

This approach runs itpss as an un-privileged agent, and starts a dedicated Endorser sub-process to endorse itpss's transactions.

Start a VON Network and a Tails server.

Start up itpss as Author (note the tails file size override, to allow testing of the revocation registry roll-over):

```bash
TAILS_FILE_COUNT=5 ./run_demo itpss --endorser-role author --revocation
```

Start up Alcie as normal:

```bash
./run_demo holder
```

You can run all of itpss's functions as normal - if you watch the console you will see that all ledger operations go through the endorser workflow.

If you issue more than 5 credentials, you will see itpss creating a new revocation registry (encluding endorser operations).


## Run holder as an Author and itpss as an Endorser

This approach sets up the endorser roles to allow manual testing using the agents' swagger pages:

- itpss runs as an Endorser (all of itpss's functions - issue credential, request proof, etc.) run normally, since itpss has ledger write access
- holder starts up with a DID aith Author privileges (no ledger write access) and itpss is setup as holder's Endorser

Start a VON Network and a Tails server.

Start up itpss as Endorser:

```bash
TAILS_FILE_COUNT=5 ./run_demo itpss --endorser-role endorser --revocation
```

Start up holder as Author:

```bash
TAILS_FILE_COUNT=5 ./run_demo holder --endorser-role author --revocation
```

Copy the invitation from itpss to holder to complete the connection.

Then in the holder shell, select option "D" and copy itpss's DID (it is the DID displayed on itpss agent startup).

This starts up the ACA-Py agents with the endorser role set (via the new command-line args) and sets up the connection between the 2 agents with appropriate configuration.

Then, in the [holder swagger page](http://localhost:8031) you can create a schema and cred def, and all the endorser steps will happen automatically.  You don't need to specify a connection id or explicitly request endorsement (ACA-Py does it all automatically based on the startup args).

If you check the endorser transaction records in either [holder](http://localhost:8031) or [itpss](http://localhost:8021) you can see that the endorser protocol executes automatically and the appropriate endorsements were endorsed before writing the transactions to the ledger.
