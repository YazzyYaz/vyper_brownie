# Trademark Smart Contract

struct Trademark:
  phrase: string[100]
  authorName: string[100]
  registrationTime: uint256(sec, positional)
  proof: bytes32

trademarkLookup: public(map(bytes32, bool))
trademarkRegistry: public(map(bytes32, Trademark))

@public
@constant
def checkTrademark(phrase: string[100]) -> bool:
  proof: bytes32 = keccak256(phrase)
  return self.trademarkLookup[proof]

@public
def registerTrademark(phraseText: string[100], author: string[100]) -> bool:
  trademark_check: bool = self.trademarkLookup[keccak256(phraseText)]
  if trademark_check == False:
    proofHash: bytes32 = keccak256(phraseText)
    self.trademarkRegistry[proofHash] = Trademark({phrase: phraseText, authorName: author, registrationTime: block.timestamp, proof: proofHash})
    self.trademarkLookup[proofHash] = True
    return True
  return False

@public
@constant
def getTrademarkData(phrase: string[100]) -> Trademark:
  return self.trademarkRegistry[keccak256(phrase)]
