

## What One learns ->

- Rust + Bitcoin is the Hansomest Combination

- SHA-256 Algorithm is used to confirm transactions


### 1. Introduction

- We should transition from a Trust-based currency to a Cryptography-based currency. Using a peer-to-peer distributed timestamp server.

### 2. Transactions

- An electronic coin is a chain of digital signatures.

### 3. Timestamp Server

- A timestamp server works by taking a hash of a block of items to be time stamped and widely publishing the has.

- Each timestamp includes the previous timestamp in its hash.

### 4. Proof of Work

- To implement a distributed tim3stamp server on a peer-to-peeer basis, we will need to use a proof-of-work system similat to Adam Back's Hascash.

- The proof-of-work involves scanning for a value that when hashed, such as with SHA-256, the hash begins with a number of zero bits.

- For our timestamp network, we implement the proof-of-work by incrementing a nonce in the block until a valie is found that gives the block's hash the required zero bits.

- As later blocks are chained after it, the work to change the block would include redoing all the blocks after it.

- The majority decision is represented by the longest chain, which has the geatest proof-of-work effort invested in it. 

- To compensate for increasing hardware speed and varying interest in running nodes over time, the proof-of-work difficulty is determined by a moving average targeting an average number of blocks per hour. If they're generated too fast, the difficulty increases.

### 5. Network

The steps to run the network are as follows:

1. New transactions are broadcast to all nodes.
2. Each node collects new transactions into a block.
3. Each node works on finding a difficult proof-of-work for its block.
4. When a node finds a proof-of-work, it broadcasts the block to all nodes.
5. Nodes accept the block only if all transactions in it are valid and not already spent.
6. Nodes express their acceptance of the block by working on creating the next block in the chain, using the hash of the accpeted block as the previous hash.

- Nodes always consider the longest chain to be the correct one and will keep working on expanding it.

- In that case, they work on the first one they received, but save the other branch in case it becomes longer. 

### 6. Incentive

- By convention, the first transaction in a block is a special transaction that starts a new coin owned by the creator of the block. This adds an incentive for nodes to support the network, and provides a way to initally distribute coins into circulation, since there is no central authority to issue them. 

- Traditionally, the first transaction in a block is called the coinbase transaction. The ammount of new bitcoin created is governed by the following equation:

<picture>
    <img src="./static/img/eq1.png">
</picture>

- The moment when the new bitcoin reward is decreased it is called, wuite appropriately, the halving. It occurs every couple of years and the lastest one in 2024 has reduced the block reward to 3.125BTC per block.

- If you add up the infinite series, you will see that the total supply of bitcoin will never exceed 21 million.

The incentive can also be funded with transaction fees. 

### 7. Reclaiming Disk Space 

- Once the latest transaciton in a coin is buried under enough blocks, the spent transactions befire it can be discarded to save disk space. To facilitate this without breaking the clok's hash, transaction are hashed in a Merkle Tree, with only the root included in the block's hash.

- Old blocks can then be compacted by stubbing off branches of the tree. The inferior hashes do not need ot be stored.

<picture>
    <img src="./static/img/eq2.png">
</picture>

- A block header with no transactions would be about 80 bytes. If we suppose blocks are generated ebery 10 minutes, that's 4.2MB per year.

### 8. Simplified Payment Verification

- It is possible to verify payments without running a full network node. A user only needs to keep a copy of the block headers of the longest proof-of-work chain which he can get by querying network nodes until he's convinced he has the longest chain,
and obtain the Merkle branch linking the transaction to the block it's timestamped in.

<picture>
    <img src="./static/img/eq3.png">
</picture>

### 9. Combining and Splitting Value

- To allow value to be split and combined, t4ransactions contain multiple inputs and outputs.

- Normally there will be either a single input from a larger previous transaction or multiple inputs combining smaller amounts, and at most two outputs: one for the payment, and one returning the change, if any, back to the sender.

<picture>
    <img src="./static/img/eq4.png">
</picture>

- It should be noted that fan-out, where a transaction depends on several transactions, and those transactions depend on many more, is not a problem here. There is never the need to extract a complete standalone copy of a transaction's history.

### 10. Privacy

- The traditional banking model achieves a level of privacy by limiting the access to information to the parties involved and the trusted third party. The necessity to announce all transactions publicly precludes this method, but privacy can still be maintained by breaking the flow of information in another place: 

By keeping public keys anonymous.

- As an additional firewall, a new key pair should be used for each transaction to keep them from being linked to a common owner.

### Calculations

- The Race Between the Honest Chain and an Atacker Chain can be characterized as a Binomial Random Walk.

- The probability of an attacker catching up from a given deficit is analogus to a Gambler's Ruin problem. We can calculate the probability of an attacker ever catches up with the honest chain as follows:

p= probability an honest node finds the next block
q= probability the attacker finds the next block
q_z= probability the attacker will ever catch up from z blocks behind

<picture>
    <img src="./static/img/eq5.png">
</picture>

- Given our assumption that p > q, the probability drops exponentially as the number of blocks the attacker has to catch up with increases.

- We now consider how long th erecipient of a new transaction needs to wait before being sufficiently certain the sender can't change the transaction. We assume the sender is an attacker who wants to make the recipient believe he paid him for a while, then switch it to pay back to himself after some time has passed. The reciever will be alerted when that happens, but the sender hopes it will be too late.

- the receiver generates a new key pair and gives the public key to the sender shortly before signing. This prevents the sender from preparing a chain of blocks ahead of time by working on it continously until he is lucky enough ot get far enough ahead, then executing the transaction at that moment. Once the transaction is sent, the dishonest sender starts working in secret on a parallel chain containing an alternate version of this transaction.

- The recipient waits until the transaction has been added to a block and z blocks have been linked afer it. he doesn't know the exact amount of progress the attacker has made, but asssumimg the honest blocks too the average expected time per block, the attacker's potential progress will be a poisson distribution with expected value:

<picture>
    <img src="./static/img/eq6.png">
</picture>

- To get the probability the attacker could still catch up now, we miltiply the Poisson density for each amount of progress he could have made by the probability he could catch up from that point:

<picture>
    <img src="./static/img/eq7.png">
</picture>

(you can check the code at ./docs/poisson)

And so on