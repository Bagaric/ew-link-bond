"""
Certificate Logic Smart-Contract interface
"""
contract = {
    "address": "0x",
    "abi": [
    {
      "constant": True,
      "inputs": [],
      "name": "cooContract",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_role",
          "type": "uint8"
        },
        {
          "name": "_caller",
          "type": "address"
        }
      ],
      "name": "isRole",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "certificateDb",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "name": "_coo",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "_certificateId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "name": "powerInW",
          "type": "uint256"
        },
        {
          "indexed": False,
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "escrow",
          "type": "address"
        }
      ],
      "name": "LogCreatedCertificate",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "_certificateId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "name": "_retire",
          "type": "bool"
        }
      ],
      "name": "LogRetireRequest",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "_certificateId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "name": "_oldOwner",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "_newOwner",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "_oldEscrow",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "_newEscrow",
          "type": "address"
        }
      ],
      "name": "LogCertificateOwnerChanged",
      "type": "event"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_database",
          "type": "address"
        }
      ],
      "name": "init",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_assetId",
          "type": "uint256"
        },
        {
          "name": "_owner",
          "type": "address"
        },
        {
          "name": "_powerInW",
          "type": "uint256"
        }
      ],
      "name": "createCertificate",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_assetId",
          "type": "uint256"
        },
        {
          "name": "_powerInW",
          "type": "uint256"
        }
      ],
      "name": "createCertificateForAssetOwner",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_id",
          "type": "uint256"
        }
      ],
      "name": "retireCertificate",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_id",
          "type": "uint256"
        },
        {
          "name": "_newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnershipByEscrow",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_id",
          "type": "uint256"
        },
        {
          "name": "_newOwner",
          "type": "address"
        }
      ],
      "name": "changeCertificateOwner",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_certificateId",
          "type": "uint256"
        }
      ],
      "name": "getCertificate",
      "outputs": [
        {
          "name": "_assetId",
          "type": "uint256"
        },
        {
          "name": "_owner",
          "type": "address"
        },
        {
          "name": "_powerInW",
          "type": "uint256"
        },
        {
          "name": "_retired",
          "type": "bool"
        },
        {
          "name": "_dataLog",
          "type": "bytes32"
        },
        {
          "name": "_coSaved",
          "type": "uint256"
        },
        {
          "name": "_escrow",
          "type": "address"
        },
        {
          "name": "_creationTime",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_sessionId",
          "type": "bytes32"
        }
      ],
      "name": "getCertificateIdBySessionId",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_certificateId",
          "type": "uint256"
        }
      ],
      "name": "getCertificateOwner",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_certificateId",
          "type": "uint256"
        }
      ],
      "name": "isRetired",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "getCertificateListLength",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_newLogic",
          "type": "address"
        }
      ],
      "name": "update",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ],
    "bytecode": "0x608060405234801561001057600080fd5b50604051602080611b91833981016040525160008054600160a060020a03909216600160a060020a0319909216919091179055611b3f806100526000396000f3006080604052600436106100c15763ffffffff60e060020a60003504166319ab453c81146100c65780631c1b8772146100e95780632c76a1b61461010a57806351640fee14610143578063544dd390146101aa57806384e814ef146101ce57806393ea5c9914610202578063af2773951461021a578063b1f2cc9d1461022f578063bb5a389e14610244578063c90ad7eb1461027f578063cbbf9f3814610294578063cf6ebee7146102b8578063d50bba1a146102d0578063daba9203146102e8575b600080fd5b3480156100d257600080fd5b506100e7600160a060020a0360043516610303565b005b3480156100f557600080fd5b506100e7600160a060020a0360043516610360565b34801561011657600080fd5b50610131600435600160a060020a0360243516604435610412565b60408051918252519081900360200190f35b34801561014f57600080fd5b5061015b6004356104d5565b60408051988952600160a060020a0397881660208a0152888101969096529315156060880152608087019290925260a086015290921660c084015260e083019190915251908190036101000190f35b3480156101b657600080fd5b506100e7600435600160a060020a03602435166105b1565b3480156101da57600080fd5b506101e6600435610a3a565b60408051600160a060020a039092168252519081900360200190f35b34801561020e57600080fd5b50610131600435610ad2565b34801561022657600080fd5b50610131610b38565b34801561023b57600080fd5b506101e6610bc8565b34801561025057600080fd5b5061026b60ff60043516600160a060020a0360243516610bd7565b604080519115158252519081900360200190f35b34801561028b57600080fd5b506101e6610dc7565b3480156102a057600080fd5b506100e7600435600160a060020a0360243516610dd6565b3480156102c457600080fd5b5061026b6004356110a3565b3480156102dc57600080fd5b506100e7600435611109565b3480156102f457600080fd5b50610131600435602435611324565b600061030f8133610bd7565b151561031a57600080fd5b600154600160a060020a03161561033057600080fd5b506001805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a0392909216919091179055565b600054600160a060020a031633811461037857600080fd5b600054600160a060020a0316331461038f57600080fd5b600154604080517fa6f9dae1000000000000000000000000000000000000000000000000000000008152600160a060020a0385811660048301529151919092169163a6f9dae191602480830192600092919082900301818387803b1580156103f657600080fd5b505af115801561040a573d6000803e3d6000fd5b505050505050565b600154600090600160a060020a0316151561042c57600080fd5b6000809054906101000a9004600160a060020a0316600160a060020a031663a34b80b06040518163ffffffff1660e060020a028152600401602060405180830381600087803b15801561047e57600080fd5b505af1158015610492573d6000803e3d6000fd5b505050506040513d60208110156104a857600080fd5b505133600160a060020a038216146104bf57600080fd5b6104cc8585856000611589565b95945050505050565b600080600080600080600080600160009054906101000a9004600160a060020a0316600160a060020a03166351640fee8a6040518263ffffffff1660e060020a0281526004018082815260200191505061010060405180830381600087803b15801561054057600080fd5b505af1158015610554573d6000803e3d6000fd5b505050506040513d61010081101561056b57600080fd5b508051602082015160408301516060840151608085015160a086015160c087015160e090970151959e50939c50919a509850965094509092509050919395975091939597565b6001546000908190600160a060020a031615156105cd57600080fd5b826000809054906101000a9004600160a060020a0316600160a060020a0316635c7460d66040518163ffffffff1660e060020a028152600401602060405180830381600087803b15801561062057600080fd5b505af1158015610634573d6000803e3d6000fd5b505050506040513d602081101561064a57600080fd5b5051604080517fecb41054000000000000000000000000000000000000000000000000000000008152600160a060020a0384811660048301529151919092169163ecb410549160248083019260209291908290030181600087803b1580156106b157600080fd5b505af11580156106c5573d6000803e3d6000fd5b505050506040513d60208110156106db57600080fd5b505115156106e857600080fd5b600154604080517f84e814ef000000000000000000000000000000000000000000000000000000008152600481018890529051600160a060020a03909216916384e814ef916024808201926020929091908290030181600087803b15801561074f57600080fd5b505af1158015610763573d6000803e3d6000fd5b505050506040513d602081101561077957600080fd5b5051600160a060020a0316331480156108225750600154604080517fcf6ebee7000000000000000000000000000000000000000000000000000000008152600481018890529051600160a060020a039092169163cf6ebee7916024808201926020929091908290030181600087803b1580156107f457600080fd5b505af1158015610808573d6000803e3d6000fd5b505050506040513d602081101561081e57600080fd5b5051155b151561082d57600080fd5b600154604080517fbdd7504800000000000000000000000000000000000000000000000000000000815260048101889052600160a060020a0387811660248301529151919092169163bdd7504891604480830192600092919082900301818387803b15801561089b57600080fd5b505af11580156108af573d6000803e3d6000fd5b5050600154604080517f84e814ef000000000000000000000000000000000000000000000000000000008152600481018a90529051600160a060020a0390921693506384e814ef92506024808201926020929091908290030181600087803b15801561091a57600080fd5b505af115801561092e573d6000803e3d6000fd5b505050506040513d602081101561094457600080fd5b5051600154604080517fd90561ba000000000000000000000000000000000000000000000000000000008152600481018990529051929550600160a060020a039091169163d90561ba916024808201926020929091908290030181600087803b1580156109b057600080fd5b505af11580156109c4573d6000803e3d6000fd5b505050506040513d60208110156109da57600080fd5b505160408051600160a060020a038087168252808816602083015283168183018190526060820152905191935086917f1d7a993900fc1aacdea8768b0618d014b58445a8255572d28b19e64bb71d95959181900360800190a25050505050565b600154604080517f84e814ef000000000000000000000000000000000000000000000000000000008152600481018490529051600092600160a060020a0316916384e814ef91602480830192602092919082900301818787803b158015610aa057600080fd5b505af1158015610ab4573d6000803e3d6000fd5b505050506040513d6020811015610aca57600080fd5b505192915050565b600154604080517f93ea5c99000000000000000000000000000000000000000000000000000000008152600481018490529051600092600160a060020a0316916393ea5c9991602480830192602092919082900301818787803b158015610aa057600080fd5b600154604080517faf2773950000000000000000000000000000000000000000000000000000000081529051600092600160a060020a03169163af27739591600480830192602092919082900301818787803b158015610b9757600080fd5b505af1158015610bab573d6000803e3d6000fd5b505050506040513d6020811015610bc157600080fd5b5051905090565b600054600160a060020a031681565b60008060006007856006811115610bea57fe5b1115610bf557600080fd5b83600160a060020a03166000809054906101000a9004600160a060020a0316600160a060020a0316638da5cb5b6040518163ffffffff1660e060020a028152600401602060405180830381600087803b158015610c5157600080fd5b505af1158015610c65573d6000803e3d6000fd5b505050506040513d6020811015610c7b57600080fd5b5051600160a060020a03161415610c955760019250610dbf565b6000809054906101000a9004600160a060020a0316600160a060020a0316635c7460d66040518163ffffffff1660e060020a028152600401602060405180830381600087803b158015610ce757600080fd5b505af1158015610cfb573d6000803e3d6000fd5b505050506040513d6020811015610d1157600080fd5b5051604080517f265209f2000000000000000000000000000000000000000000000000000000008152600160a060020a0387811660048301529151919092169163265209f29160248083019260209291908290030181600087803b158015610d7857600080fd5b505af1158015610d8c573d6000803e3d6000fd5b505050506040513d6020811015610da257600080fd5b50519150846006811115610db257fe5b60020a8281161515935090505b505092915050565b600154600160a060020a031681565b60015460009081908190600160a060020a03161515610df457600080fd5b6000809054906101000a9004600160a060020a0316600160a060020a031663a34b80b06040518163ffffffff1660e060020a028152600401602060405180830381600087803b158015610e4657600080fd5b505af1158015610e5a573d6000803e3d6000fd5b505050506040513d6020811015610e7057600080fd5b505133600160a060020a03821614610e8757600080fd5b600154604080517f51640fee000000000000000000000000000000000000000000000000000000008152600481018990529051600160a060020a03909216916351640fee91602480820192610100929091908290030181600087803b158015610eef57600080fd5b505af1158015610f03573d6000803e3d6000fd5b505050506040513d610100811015610f1a57600080fd5b506020810151606082015160c09092015190955090935091508215610f3e57600080fd5b600154604080517fbdd7504800000000000000000000000000000000000000000000000000000000815260048101899052600160a060020a0388811660248301529151919092169163bdd7504891604480830192600092919082900301818387803b158015610fac57600080fd5b505af1158015610fc0573d6000803e3d6000fd5b5050600154604080517f06ec8982000000000000000000000000000000000000000000000000000000008152600481018b90526000602482018190529151600160a060020a0390931694506306ec898293506044808201939182900301818387803b15801561102e57600080fd5b505af1158015611042573d6000803e3d6000fd5b505060408051600160a060020a038089168252808a1660208301528616818301526000606082015290518993507f1d7a993900fc1aacdea8768b0618d014b58445a8255572d28b19e64bb71d959592509081900360800190a2505050505050565b600154604080517fcf6ebee7000000000000000000000000000000000000000000000000000000008152600481018490529051600092600160a060020a03169163cf6ebee791602480830192602092919082900301818787803b158015610aa057600080fd5b6001546000908190600160a060020a0316151561112557600080fd5b600154604080517f51640fee000000000000000000000000000000000000000000000000000000008152600481018690529051600160a060020a03909216916351640fee91602480820192610100929091908290030181600087803b15801561118d57600080fd5b505af11580156111a1573d6000803e3d6000fd5b505050506040513d6101008110156111b857600080fd5b5060208101516060909101519092509050600160a060020a03821633146111de57600080fd5b80151561131f57600154604080517f06ec8982000000000000000000000000000000000000000000000000000000008152600481018690526000602482018190529151600160a060020a03909316926306ec89829260448084019391929182900301818387803b15801561125157600080fd5b505af1158015611265573d6000803e3d6000fd5b5050600154604080517fd50bba1a000000000000000000000000000000000000000000000000000000008152600481018890529051600160a060020a03909216935063d50bba1a925060248082019260009290919082900301818387803b1580156112cf57600080fd5b505af11580156112e3573d6000803e3d6000fd5b5050604080516001815290518693507f4c9e4e2878404da5e23cb4c5ef447b8e31155efa1229be3e2a8541cc5aab275d92509081900360200190a25b505050565b60008060066113338133610bd7565b151561133e57600080fd5b600154600160a060020a0316151561135557600080fd5b6000809054906101000a9004600160a060020a0316600160a060020a03166324a793c46040518163ffffffff1660e060020a028152600401602060405180830381600087803b1580156113a757600080fd5b505af11580156113bb573d6000803e3d6000fd5b505050506040513d60208110156113d157600080fd5b5051604080517fc6bc1a76000000000000000000000000000000000000000000000000000000008152600481018890529051600160a060020a039092169163c6bc1a76916024808201926020929091908290030181600087803b15801561143757600080fd5b505af115801561144b573d6000803e3d6000fd5b505050506040513d602081101561146157600080fd5b5051151561146e57600080fd5b6000809054906101000a9004600160a060020a0316600160a060020a03166324a793c46040518163ffffffff1660e060020a028152600401602060405180830381600087803b1580156114c057600080fd5b505af11580156114d4573d6000803e3d6000fd5b505050506040513d60208110156114ea57600080fd5b5051604080517fade1e992000000000000000000000000000000000000000000000000000000008152600481018890529051600160a060020a039092169163ade1e9929160248082019260c0929091908290030181600087803b15801561155057600080fd5b505af1158015611564573d6000803e3d6000fd5b505050506040513d60c081101561157a57600080fd5b506020015191506104cc858386335b600154600090819081908190600160a060020a031615156115a957600080fd5b6000809054906101000a9004600160a060020a0316600160a060020a03166324a793c46040518163ffffffff1660e060020a028152600401602060405180830381600087803b1580156115fb57600080fd5b505af115801561160f573d6000803e3d6000fd5b505050506040513d602081101561162557600080fd5b5051604080517f76b240ee000000000000000000000000000000000000000000000000000000008152600481018b9052602481018990529051600160a060020a03909216916376b240ee916044808201926020929091908290030181600087803b15801561169257600080fd5b505af11580156116a6573d6000803e3d6000fd5b505050506040513d60208110156116bc57600080fd5b505160008054604080517f24a793c40000000000000000000000000000000000000000000000000000000081529051939650600160a060020a03909116926324a793c492600480840193602093929083900390910190829087803b15801561172357600080fd5b505af1158015611737573d6000803e3d6000fd5b505050506040513d602081101561174d57600080fd5b5051604080517f1e13970b000000000000000000000000000000000000000000000000000000008152600481018b9052602481018990529051600160a060020a0390921691631e13970b916044808201926020929091908290030181600087803b1580156117ba57600080fd5b505af11580156117ce573d6000803e3d6000fd5b505050506040513d60208110156117e457600080fd5b505115156117f157600080fd5b6000809054906101000a9004600160a060020a0316600160a060020a03166324a793c46040518163ffffffff1660e060020a028152600401602060405180830381600087803b15801561184357600080fd5b505af1158015611857573d6000803e3d6000fd5b505050506040513d602081101561186d57600080fd5b5051604080517ff7105c05000000000000000000000000000000000000000000000000000000008152600481018b90529051600160a060020a039092169163f7105c05916024808201926020929091908290030181600087803b1580156118d357600080fd5b505af11580156118e7573d6000803e3d6000fd5b505050506040513d60208110156118fd57600080fd5b5051600154604080517f42c366a5000000000000000000000000000000000000000000000000000000008152600481018c9052600160a060020a038b81166024830152604482018b9052606482018590526084820188905289811660a483015291519395509116916342c366a59160c4808201926020929091908290030181600087803b15801561198d57600080fd5b505af11580156119a1573d6000803e3d6000fd5b505050506040513d60208110156119b757600080fd5b505160408051888152600160a060020a03808b166020830152881681830152905191925082917f05763c5a99ca059f9fba5a40ed660f24ddd30b3a3d6f367bc071fbc22a79ffaf9181900360600190a26000809054906101000a9004600160a060020a0316600160a060020a03166324a793c46040518163ffffffff1660e060020a028152600401602060405180830381600087803b158015611a5957600080fd5b505af1158015611a6d573d6000803e3d6000fd5b505050506040513d6020811015611a8357600080fd5b5051604080517f50ddca55000000000000000000000000000000000000000000000000000000008152600481018b9052602481018690529051600160a060020a03909216916350ddca559160448082019260009290919082900301818387803b158015611aef57600080fd5b505af1158015611b03573d6000803e3d6000fd5b50929a99505050505050505050505600a165627a7a723058203fa18a25ccb260d6fe83e94e3af5e1670fb25dce432c8e1d65f6593d24721d460029",
}