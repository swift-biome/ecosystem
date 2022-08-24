class semver:
    def __init__(self, string, revision = None):
        self.version = string
        if revision is None:
            self.pin = 'exact: "{0}"'.format(string)
        else:
            self.pin = 'revision: "{0}"'.format(revision)
    
    def __str__(self): 
        return self.version

class swift:
    def __init__(self, string):
        self.version = string
        self.pin = 'revision: "{0}"'.format(str(self))
    
    def __str__(self): 
        return 'swift-' + self.version

packages = (
    (
        'https://github.com/kelvin13', 'swift-grammar', 'Swift Grammar',
        (
            (
                semver('0.1.4'), 
                (
                    'Grammar',
                ),
                ()
            ),
            (
                semver('0.1.5'), 
                (
                    'Grammar',
                ),
                ()
            ),
            (
                semver('0.2.0'), 
                (
                    'Grammar',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/kelvin13', 'swift-json', 'Swift JSON',
        (
            (
                semver('0.2.2'), 
                (
                    'JSON',
                ),
                ()
            ),
            (
                semver('0.3.0', revision = '48ab4fc74c9b1800f481b246dc382c7d9fa522bf'), 
                (
                    'JSON',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-system', 'SwiftSystem',
        (
            (
                semver('1.1.0'), 
                (
                    'SystemPackage',
                ),
                ()
            ),
            (
                semver('1.1.1'), 
                (
                    'SystemPackage',
                ),
                ()
            ),
            (
                semver('1.2.0'), 
                (
                    'SystemPackage',
                ),
                ()
            ),
            (
                semver('1.2.1'), 
                (
                    'SystemPackage',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-nio', 'SwiftNIO',
        (
            (
                semver('2.38.0'), 
                (
                    'NIO',
                    'NIOCore',
                    'NIOConcurrencyHelpers',
                    'NIOFoundationCompat',
                    'NIOEmbedded',
                    'NIOHTTP1',
                    'NIOPosix',
                    'NIOTLS',
                    'NIOWebSocket',
                ),
                (
                    '_NIODataStructures',
                )
            ),
            (
                semver('2.39.0'), 
                (
                    'NIO',
                    'NIOCore',
                    'NIOConcurrencyHelpers',
                    'NIOFoundationCompat',
                    'NIOEmbedded',
                    'NIOHTTP1',
                    'NIOPosix',
                    'NIOTLS',
                    'NIOWebSocket',
                ),
                (
                    '_NIODataStructures',
                )
            ),
            (
                semver('2.40.0'), 
                (
                    'NIO',
                    'NIOCore',
                    'NIOConcurrencyHelpers',
                    'NIOFoundationCompat',
                    'NIOEmbedded',
                    'NIOHTTP1',
                    'NIOPosix',
                    'NIOTLS',
                    'NIOWebSocket',
                ),
                (
                    '_NIODataStructures',
                )
            ),
            (
                semver('2.41.0'), 
                (
                    'NIO',
                    'NIOCore',
                    'NIOConcurrencyHelpers',
                    'NIOFoundationCompat',
                    'NIOEmbedded',
                    'NIOHTTP1',
                    'NIOPosix',
                    'NIOTLS',
                    'NIOWebSocket',
                ),
                (
                    '_NIODataStructures',
                )
            ),
            (
                semver('2.41.1'), 
                (
                    'NIO',
                    'NIOCore',
                    'NIOConcurrencyHelpers',
                    'NIOFoundationCompat',
                    'NIOEmbedded',
                    'NIOHTTP1',
                    'NIOPosix',
                    'NIOTLS',
                    'NIOWebSocket',
                ),
                (
                    '_NIODataStructures',
                )
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-nio-ssl', 'SwiftNIO SSL',
        (
            (
                semver('2.20.2'), 
                (
                    'NIOSSL',
                ),
                ()
            ),
            (
                semver('2.21.0'), 
                (
                    'NIOSSL',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-atomics', 'Swift Atomics',
        (
            (
                semver('1.0.2'), 
                (
                    'Atomics',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-numerics', 'Swift Numerics',
        (
            (
                semver('1.0.2'), 
                (
                    'ComplexModule',
                    'RealModule',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-collections', 'Swift Collections',
        (
            (
                semver('1.0.2'), 
                (
                    'DequeModule',
                    'OrderedCollections',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-argument-parser', 'ArgumentParser',
        (
            (
                semver('1.1.3'), 
                (
                    'ArgumentParser',
                ),
                (
                    'ArgumentParserToolInfo',
                )
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-syntax', 'SwiftSyntax',
        (
            (
                swift('DEVELOPMENT-SNAPSHOT-2022-03-13-a'), 
                (
                    'SwiftSyntax',
                    'SwiftSyntaxParser',
                    'SwiftSyntaxBuilder',
                ),
                ()
            ),
            (
                swift('DEVELOPMENT-SNAPSHOT-2022-06-20-a'), 
                (
                    'SwiftSyntax',
                    'SwiftSyntaxParser',
                    'SwiftSyntaxBuilder',
                ),
                ()
            ),
            (
                swift('DEVELOPMENT-SNAPSHOT-2022-08-15-a'), 
                (
                    'SwiftSyntax',
                    'SwiftSyntaxParser',
                    'SwiftSyntaxBuilder',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-markdown', 'Swift Markdown',
        (
            (
                swift('DEVELOPMENT-SNAPSHOT-2022-03-13-a'), 
                (
                    'Markdown',
                ),
                ()
            ),
            (
                swift('DEVELOPMENT-SNAPSHOT-2022-06-20-a'), 
                (
                    'Markdown',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-log', 'SwiftLog',
        (
            (
                semver('1.4.2'), 
                (
                    'Logging',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/apple', 'swift-metrics', 'SwiftMetrics',
        (
            (
                semver('2.3.1'), 
                (
                    'CoreMetrics',
                    'Metrics',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/orlandos-nl', 'niodns', 'SwiftNIO DNS',
        (
            (
                semver('2.0.7'), 
                (
                    'DNSClient',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/orlandos-nl', 'bson', 'Swift BSON',
        (
            (
                semver('8.0.1'), 
                (
                    'BSON',
                ),
                ()
            ),
        )
    ),
    (
        'https://github.com/orlandos-nl', 'mongokitten', 'MongoKitten',
        (
            (
                semver('7.0.1'), 
                (
                    'MongoCore',
                    'MongoKitten',
                    'MongoClient',
                    'Meow',
                ),
                (
                    'MongoKittenCore',
                    '_MongoKittenCrypto',
                )
            ),
            (
                semver('7.1.0'), 
                (
                    'MongoCore',
                    'MongoKitten',
                    'MongoClient',
                    'Meow',
                ),
                (
                    'MongoKittenCore',
                    '_MongoKittenCrypto',
                )
            ),
            (
                semver('7.2.0'), 
                (
                    'MongoCore',
                    'MongoKitten',
                    'MongoClient',
                    'Meow',
                ),
                (
                    'MongoKittenCore',
                    '_MongoKittenCrypto',
                )
            ),
            (
                semver('7.2.1'), 
                (
                    'MongoCore',
                    'MongoKitten',
                    'MongoClient',
                    'Meow',
                ),
                (
                    'MongoKittenCore',
                    '_MongoKittenCrypto',
                )
            ),
        )
    ),
)