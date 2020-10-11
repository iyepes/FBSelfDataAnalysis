def accent_replace(post):
    post = post.replace('Ã±', 'ñ')
    post = post.replace('Ã¡', 'á')
    post = post.replace('Ã©', 'é')
    post = post.replace('Ã­', 'í')
    post = post.replace('Ã³', 'ó')
    post = post.replace('Ãº', 'ú')
    post = post.replace('Â¿', '¿')
    post = post.replace('â', '\"')
    post = post.replace('â ', '\" ')
    post = post.replace('â.', '\".')
    post = post.replace('.â', '.\"')
    post = post.replace('â', '\'')
    post = post.replace('Ã¼', 'ü')
    post = post.replace('Â¡', '¡')
    post = post.replace('Ã\x81', 'Á')
    post = post.replace('\n', ' ')
    post = post.replace('Â´', '\'')
    post = post.replace('â\x80\x9c', '\"')
    post = post.replace('â\x80\x9d', '\"')
    post = post.replace('ð\x9f\x98¢', '\"')
    return post

def emoticons_replace(post):
    post = post.replace('\u00f0\u009f\u0098\u0081', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0082', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0083', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0084', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0085', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0086', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0089', ' ')
    post = post.replace('\u00f0\u009f\u0098\u008a', ' ')
    post = post.replace('\u00f0\u009f\u0098\u008b', ' ')
    post = post.replace('\u00f0\u009f\u0098\u008c', ' ')
    post = post.replace('\u00f0\u009f\u0098\u008d', ' ')
    post = post.replace('\u00f0\u009f\u0098\u008f', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0092', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0093', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0094', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0096', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0098', ' ')
    post = post.replace('\u00f0\u009f\u0098\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0098\u009c', ' ')
    post = post.replace('\u00f0\u009f\u0098\u009d', ' ')
    post = post.replace('\u00f0\u009f\u0098\u009e', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00be', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00bf', ' ')
    post = post.replace('\u00f0\u009f\u0099\u0080', ' ')
    post = post.replace('\u00f0\u009f\u0099\u0085', ' ')
    post = post.replace('\u00f0\u009f\u0099\u0086', ' ')
    post = post.replace('\u00f0\u009f\u0099\u0087', ' ')
    post = post.replace('\u00f0\u009f\u0099\u0088', ' ')
    post = post.replace('\u00f0\u009f\u0099\u0089', ' ')
    post = post.replace('\u00f0\u009f\u0099\u008a', ' ')
    post = post.replace('\u00f0\u009f\u0099\u008b', ' ')
    post = post.replace('\u00f0\u009f\u0099\u008c', ' ')
    post = post.replace('\u00f0\u009f\u0099\u008d', ' ')
    post = post.replace('\u00f0\u009f\u0099\u008e', ' ')
    post = post.replace('\u00f0\u009f\u0099\u008f', ' ')
    post = post.replace('\u00e2\u009c\u0082', ' ')
    post = post.replace('\u00e2\u009c\u0085', ' ')
    post = post.replace('\u00e2\u009c\u0088', ' ')
    post = post.replace('\u00e2\u009c\u0089', ' ')
    post = post.replace('\u00e2\u009c\u008a', ' ')
    post = post.replace('\u00e2\u009c\u008b', ' ')
    post = post.replace('\u00e2\u009c\u008c', ' ')
    post = post.replace('\u00e2\u009c\u008f', ' ')
    post = post.replace('\u00e2\u009c\u0092', ' ')
    post = post.replace('\u00e2\u009c\u0094', ' ')
    post = post.replace('\u00e2\u009c\u0096', ' ')
    post = post.replace('\u00e2\u009c\u00a8', ' ')
    post = post.replace('\u00e2\u009c\u00b3', ' ')
    post = post.replace('\u00e2\u009c\u00b4', ' ')
    post = post.replace('\u00e2\u009d\u0084', ' ')
    post = post.replace('\u00e2\u009d\u0087', ' ')
    post = post.replace('\u00e2\u009d\u008c', ' ')
    post = post.replace('\u00e2\u009d\u008e', ' ')
    post = post.replace('\u00e2\u009d\u0093', ' ')
    post = post.replace('\u00e2\u009d\u0094', ' ')
    post = post.replace('\u00e2\u009d\u0095', ' ')
    post = post.replace('\u00e2\u009d\u0097', ' ')
    post = post.replace('\u00e2\u009d\u00a4', ' ')
    post = post.replace('\u00e2\u009e\u0095', ' ')
    post = post.replace('\u00e2\u009e\u0096', ' ')
    post = post.replace('\u00e2\u009e\u0097', ' ')
    post = post.replace('\u00e2\u009e\u00a1', ' ')
    post = post.replace('\u00e2\u009e\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0080', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0083', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0084', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0085', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0087', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0089', ' ')
    post = post.replace('\u00f0\u009f\u009a\u008c', ' ')
    post = post.replace('\u00f0\u009f\u009a\u008f', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0091', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0092', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0093', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0095', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0097', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0099', ' ')
    post = post.replace('\u00f0\u009f\u009a\u009a', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00be', ' ')
    post = post.replace('\u00f0\u009f\u009b\u0080', ' ')
    post = post.replace('\u00e2\u0093\u0082', ' ')
    post = post.replace('\u00f0\u009f\u0085\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u0085\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u0085\u00be', ' ')
    post = post.replace('\u00f0\u009f\u0085\u00bf', ' ')
    post = post.replace('\u00f0\u009f\u0086\u008e', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0091', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0092', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0093', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0094', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0095', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0096', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0097', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0098', ' ')
    post = post.replace('\u00f0\u009f\u0086\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0086\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00a9\u00f0\u009f\u0087\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00ac\u00f0\u009f\u0087\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00a8\u00f0\u009f\u0087\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00af\u00f0\u009f\u0087\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00ab\u00f0\u009f\u0087\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00b0\u00f0\u009f\u0087\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00aa\u00f0\u009f\u0087\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00ae\u00f0\u009f\u0087\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00b7\u00f0\u009f\u0087\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u0087\u00ba\u00f0\u009f\u0087\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u0088\u0081', ' ')
    post = post.replace('\u00f0\u009f\u0088\u0082', ' ')
    post = post.replace('\u00f0\u009f\u0088\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00af', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u0088\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u0089\u0090', ' ')
    post = post.replace('\u00f0\u009f\u0089\u0091', ' ')
    post = post.replace('\u00c2\u00a9', ' ')
    post = post.replace('\u00c2\u00ae', ' ')
    post = post.replace('\u00e2\u0080\u00bc', ' ')
    post = post.replace('\u00e2\u0081\u0089', ' ')
    post = post.replace('\u0023\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0038\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0039\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0037\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0030\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0036\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0035\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0034\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0033\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0032\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u0031\u00e2\u0083\u00a3', ' ')
    post = post.replace('\u00e2\u0084\u00a2', ' ')
    post = post.replace('\u00e2\u0084\u00b9', ' ')
    post = post.replace('\u00e2\u0086\u0094', ' ')
    post = post.replace('\u00e2\u0086\u0095', ' ')
    post = post.replace('\u00e2\u0086\u0096', ' ')
    post = post.replace('\u00e2\u0086\u0097', ' ')
    post = post.replace('\u00e2\u0086\u0098', ' ')
    post = post.replace('\u00e2\u0086\u0099', ' ')
    post = post.replace('\u00e2\u0086\u00a9', ' ')
    post = post.replace('\u00e2\u0086\u00aa', ' ')
    post = post.replace('\u00e2\u008c\u009a', ' ')
    post = post.replace('\u00e2\u008c\u009b', ' ')
    post = post.replace('\u00e2\u008f\u00a9', ' ')
    post = post.replace('\u00e2\u008f\u00aa', ' ')
    post = post.replace('\u00e2\u008f\u00ab', ' ')
    post = post.replace('\u00e2\u008f\u00ac', ' ')
    post = post.replace('\u00e2\u008f\u00b0', ' ')
    post = post.replace('\u00e2\u008f\u00b3', ' ')
    post = post.replace('\u00e2\u0096\u00aa', ' ')
    post = post.replace('\u00e2\u0096\u00ab', ' ')
    post = post.replace('\u00e2\u0096\u00b6', ' ')
    post = post.replace('\u00e2\u0097\u0080', ' ')
    post = post.replace('\u00e2\u0097\u00bb', ' ')
    post = post.replace('\u00e2\u0097\u00bc', ' ')
    post = post.replace('\u00e2\u0097\u00bd', ' ')
    post = post.replace('\u00e2\u0097\u00be', ' ')
    post = post.replace('\u00e2\u0098\u0080', ' ')
    post = post.replace('\u00e2\u0098\u0081', ' ')
    post = post.replace('\u00e2\u0098\u008e', ' ')
    post = post.replace('\u00e2\u0098\u0091', ' ')
    post = post.replace('\u00e2\u0098\u0094', ' ')
    post = post.replace('\u00e2\u0098\u0095', ' ')
    post = post.replace('\u00e2\u0098\u009d', ' ')
    post = post.replace('\u00e2\u0098\u00ba', ' ')
    post = post.replace('\u00e2\u0099\u0088', ' ')
    post = post.replace('\u00e2\u0099\u0089', ' ')
    post = post.replace('\u00e2\u0099\u008a', ' ')
    post = post.replace('\u00e2\u0099\u008b', ' ')
    post = post.replace('\u00e2\u0099\u008c', ' ')
    post = post.replace('\u00e2\u0099\u008d', ' ')
    post = post.replace('\u00e2\u0099\u008e', ' ')
    post = post.replace('\u00e2\u0099\u008f', ' ')
    post = post.replace('\u00e2\u0099\u0090', ' ')
    post = post.replace('\u00e2\u0099\u0091', ' ')
    post = post.replace('\u00e2\u0099\u0092', ' ')
    post = post.replace('\u00e2\u0099\u0093', ' ')
    post = post.replace('\u00e2\u0099\u00a0', ' ')
    post = post.replace('\u00e2\u0099\u00a3', ' ')
    post = post.replace('\u00e2\u0099\u00a5', ' ')
    post = post.replace('\u00e2\u0099\u00a6', ' ')
    post = post.replace('\u00e2\u0099\u00a8', ' ')
    post = post.replace('\u00e2\u0099\u00bb', ' ')
    post = post.replace('\u00e2\u0099\u00bf', ' ')
    post = post.replace('\u00e2\u009a\u0093', ' ')
    post = post.replace('\u00e2\u009a\u00a0', ' ')
    post = post.replace('\u00e2\u009a\u00a1', ' ')
    post = post.replace('\u00e2\u009a\u00aa', ' ')
    post = post.replace('\u00e2\u009a\u00ab', ' ')
    post = post.replace('\u00e2\u009a\u00bd', ' ')
    post = post.replace('\u00e2\u009a\u00be', ' ')
    post = post.replace('\u00e2\u009b\u0084', ' ')
    post = post.replace('\u00e2\u009b\u0085', ' ')
    post = post.replace('\u00e2\u009b\u008e', ' ')
    post = post.replace('\u00e2\u009b\u0094', ' ')
    post = post.replace('\u00e2\u009b\u00aa', ' ')
    post = post.replace('\u00e2\u009b\u00b2', ' ')
    post = post.replace('\u00e2\u009b\u00b3', ' ')
    post = post.replace('\u00e2\u009b\u00b5', ' ')
    post = post.replace('\u00e2\u009b\u00ba', ' ')
    post = post.replace('\u00e2\u009b\u00bd', ' ')
    post = post.replace('\u00e2\u00a4\u00b4', ' ')
    post = post.replace('\u00e2\u00a4\u00b5', ' ')
    post = post.replace('\u00e2\u00ac\u0085', ' ')
    post = post.replace('\u00e2\u00ac\u0086', ' ')
    post = post.replace('\u00e2\u00ac\u0087', ' ')
    post = post.replace('\u00e2\u00ac\u009b', ' ')
    post = post.replace('\u00e2\u00ac\u009c', ' ')
    post = post.replace('\u00e2\u00ad\u0090', ' ')
    post = post.replace('\u00e2\u00ad\u0095', ' ')
    post = post.replace('\u00e3\u0080\u00b0', ' ')
    post = post.replace('\u00e3\u0080\u00bd', ' ')
    post = post.replace('\u00e3\u008a\u0097', ' ')
    post = post.replace('\u00e3\u008a\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0080\u0084', ' ')
    post = post.replace('\u00f0\u009f\u0083\u008f', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0080', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0081', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0082', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0083', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0084', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0085', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0086', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0087', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0088', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0089', ' ')
    post = post.replace('\u00f0\u009f\u008c\u008a', ' ')
    post = post.replace('\u00f0\u009f\u008c\u008b', ' ')
    post = post.replace('\u00f0\u009f\u008c\u008c', ' ')
    post = post.replace('\u00f0\u009f\u008c\u008f', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0091', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0093', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0094', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0095', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0099', ' ')
    post = post.replace('\u00f0\u009f\u008c\u009b', ' ')
    post = post.replace('\u00f0\u009f\u008c\u009f', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00be', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00bf', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0080', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0081', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0082', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0083', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0084', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0085', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0086', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0087', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0088', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0089', ' ')
    post = post.replace('\u00f0\u009f\u008d\u008a', ' ')
    post = post.replace('\u00f0\u009f\u008d\u008c', ' ')
    post = post.replace('\u00f0\u009f\u008d\u008d', ' ')
    post = post.replace('\u00f0\u009f\u008d\u008e', ' ')
    post = post.replace('\u00f0\u009f\u008d\u008f', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0091', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0092', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0093', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0094', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0095', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0096', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0097', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0098', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0099', ' ')
    post = post.replace('\u00f0\u009f\u008d\u009a', ' ')
    post = post.replace('\u00f0\u009f\u008d\u009b', ' ')
    post = post.replace('\u00f0\u009f\u008d\u009c', ' ')
    post = post.replace('\u00f0\u009f\u008d\u009d', ' ')
    post = post.replace('\u00f0\u009f\u008d\u009e', ' ')
    post = post.replace('\u00f0\u009f\u008d\u009f', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00af', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0080', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0081', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0082', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0083', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0084', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0085', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0086', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0087', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0088', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0089', ' ')
    post = post.replace('\u00f0\u009f\u008e\u008a', ' ')
    post = post.replace('\u00f0\u009f\u008e\u008b', ' ')
    post = post.replace('\u00f0\u009f\u008e\u008c', ' ')
    post = post.replace('\u00f0\u009f\u008e\u008d', ' ')
    post = post.replace('\u00f0\u009f\u008e\u008e', ' ')
    post = post.replace('\u00f0\u009f\u008e\u008f', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0090', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0091', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0092', ' ')
    post = post.replace('\u00f0\u009f\u008e\u0093', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00af', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00be', ' ')
    post = post.replace('\u00f0\u009f\u008e\u00bf', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0080', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0081', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0082', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0083', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0084', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0086', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0088', ' ')
    post = post.replace('\u00f0\u009f\u008f\u008a', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00af', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u0090\u008c', ' ')
    post = post.replace('\u00f0\u009f\u0090\u008d', ' ')
    post = post.replace('\u00f0\u009f\u0090\u008e', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0091', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0092', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0094', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0097', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0098', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0090\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0090\u009b', ' ')
    post = post.replace('\u00f0\u009f\u0090\u009c', ' ')
    post = post.replace('\u00f0\u009f\u0090\u009d', ' ')
    post = post.replace('\u00f0\u009f\u0090\u009e', ' ')
    post = post.replace('\u00f0\u009f\u0090\u009f', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00af', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00be', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0080', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0082', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0083', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0084', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0085', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0086', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0087', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0088', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0089', ' ')
    post = post.replace('\u00f0\u009f\u0091\u008a', ' ')
    post = post.replace('\u00f0\u009f\u0091\u008b', ' ')
    post = post.replace('\u00f0\u009f\u0091\u008c', ' ')
    post = post.replace('\u00f0\u009f\u0091\u008d', ' ')
    post = post.replace('\u00f0\u009f\u0091\u008e', ' ')
    post = post.replace('\u00f0\u009f\u0091\u008f', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0090', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0091', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0092', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0093', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0094', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0095', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0096', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0097', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0098', ' ')
    post = post.replace('\u00f0\u009f\u0091\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0091\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0091\u009b', ' ')
    post = post.replace('\u00f0\u009f\u0091\u009c', ' ')
    post = post.replace('\u00f0\u009f\u0091\u009d', ' ')
    post = post.replace('\u00f0\u009f\u0091\u009e', ' ')
    post = post.replace('\u00f0\u009f\u0091\u009f', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00af', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00be', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00bf', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0080', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0081', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0082', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0083', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0084', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0085', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0086', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0087', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0088', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0089', ' ')
    post = post.replace('\u00f0\u009f\u0092\u008a', ' ')
    post = post.replace('\u00f0\u009f\u0092\u008b', ' ')
    post = post.replace('\u00f0\u009f\u0092\u008c', ' ')
    post = post.replace('\u00f0\u009f\u0092\u008d', ' ')
    post = post.replace('\u00f0\u009f\u0092\u008e', ' ')
    post = post.replace('\u00f0\u009f\u0092\u008f', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0090', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0091', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0092', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0093', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0094', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0095', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0096', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0097', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0098', ' ')
    post = post.replace('\u00f0\u009f\u0092\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0092\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0092\u009b', ' ')
    post = post.replace('\u00f0\u009f\u0092\u009c', ' ')
    post = post.replace('\u00f0\u009f\u0092\u009d', ' ')
    post = post.replace('\u00f0\u009f\u0092\u009e', ' ')
    post = post.replace('\u00f0\u009f\u0092\u009f', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00af', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00be', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00bf', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0080', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0081', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0082', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0083', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0084', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0085', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0086', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0087', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0088', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0089', ' ')
    post = post.replace('\u00f0\u009f\u0093\u008a', ' ')
    post = post.replace('\u00f0\u009f\u0093\u008b', ' ')
    post = post.replace('\u00f0\u009f\u0093\u008c', ' ')
    post = post.replace('\u00f0\u009f\u0093\u008d', ' ')
    post = post.replace('\u00f0\u009f\u0093\u008e', ' ')
    post = post.replace('\u00f0\u009f\u0093\u008f', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0090', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0091', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0092', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0093', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0094', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0095', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0096', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0097', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0098', ' ')
    post = post.replace('\u00f0\u009f\u0093\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0093\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0093\u009b', ' ')
    post = post.replace('\u00f0\u009f\u0093\u009c', ' ')
    post = post.replace('\u00f0\u009f\u0093\u009d', ' ')
    post = post.replace('\u00f0\u009f\u0093\u009e', ' ')
    post = post.replace('\u00f0\u009f\u0093\u009f', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0083', ' ')
    post = post.replace('\u00f0\u009f\u0094\u008a', ' ')
    post = post.replace('\u00f0\u009f\u0094\u008b', ' ')
    post = post.replace('\u00f0\u009f\u0094\u008c', ' ')
    post = post.replace('\u00f0\u009f\u0094\u008d', ' ')
    post = post.replace('\u00f0\u009f\u0094\u008e', ' ')
    post = post.replace('\u00f0\u009f\u0094\u008f', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0090', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0091', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0092', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0093', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0094', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0096', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0097', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0098', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0094\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0094\u009b', ' ')
    post = post.replace('\u00f0\u009f\u0094\u009c', ' ')
    post = post.replace('\u00f0\u009f\u0094\u009d', ' ')
    post = post.replace('\u00f0\u009f\u0094\u009e', ' ')
    post = post.replace('\u00f0\u009f\u0094\u009f', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a8', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00a9', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00ab', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00af', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00b9', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00ba', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0090', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0091', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0092', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0093', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0094', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0095', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0096', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0097', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0098', ' ')
    post = post.replace('\u00f0\u009f\u0095\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0095\u009a', ' ')
    post = post.replace('\u00f0\u009f\u0095\u009b', ' ')
    post = post.replace('\u00f0\u009f\u0097\u00bb', ' ')
    post = post.replace('\u00f0\u009f\u0097\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u0097\u00bd', ' ')
    post = post.replace('\u00f0\u009f\u0097\u00be', ' ')
    post = post.replace('\u00f0\u009f\u0097\u00bf', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0080', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0087', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0088', ' ')
    post = post.replace('\u00f0\u009f\u0098\u008e', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0090', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0091', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0095', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0097', ' ')
    post = post.replace('\u00f0\u009f\u0098\u0099', ' ')
    post = post.replace('\u00f0\u009f\u0098\u009b', ' ')
    post = post.replace('\u00f0\u009f\u0098\u009f', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00a7', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00af', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u0098\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0081', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0082', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0086', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0088', ' ')
    post = post.replace('\u00f0\u009f\u009a\u008a', ' ')
    post = post.replace('\u00f0\u009f\u009a\u008d', ' ')
    post = post.replace('\u00f0\u009f\u009a\u008e', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0090', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0094', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0096', ' ')
    post = post.replace('\u00f0\u009f\u009a\u0098', ' ')
    post = post.replace('\u00f0\u009f\u009a\u009b', ' ')
    post = post.replace('\u00f0\u009f\u009a\u009c', ' ')
    post = post.replace('\u00f0\u009f\u009a\u009d', ' ')
    post = post.replace('\u00f0\u009f\u009a\u009e', ' ')
    post = post.replace('\u00f0\u009f\u009a\u009f', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00ae', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00af', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b0', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b1', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b4', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00b8', ' ')
    post = post.replace('\u00f0\u009f\u009a\u00bf', ' ')
    post = post.replace('\u00f0\u009f\u009b\u0081', ' ')
    post = post.replace('\u00f0\u009f\u009b\u0082', ' ')
    post = post.replace('\u00f0\u009f\u009b\u0083', ' ')
    post = post.replace('\u00f0\u009f\u009b\u0084', ' ')
    post = post.replace('\u00f0\u009f\u009b\u0085', ' ')
    post = post.replace('\u00f0\u009f\u008c\u008d', ' ')
    post = post.replace('\u00f0\u009f\u008c\u008e', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0090', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0092', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0096', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0097', ' ')
    post = post.replace('\u00f0\u009f\u008c\u0098', ' ')
    post = post.replace('\u00f0\u009f\u008c\u009a', ' ')
    post = post.replace('\u00f0\u009f\u008c\u009c', ' ')
    post = post.replace('\u00f0\u009f\u008c\u009d', ' ')
    post = post.replace('\u00f0\u009f\u008c\u009e', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b2', ' ')
    post = post.replace('\u00f0\u009f\u008c\u00b3', ' ')
    post = post.replace('\u00f0\u009f\u008d\u008b', ' ')
    post = post.replace('\u00f0\u009f\u008d\u0090', ' ')
    post = post.replace('\u00f0\u009f\u008d\u00bc', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0087', ' ')
    post = post.replace('\u00f0\u009f\u008f\u0089', ' ')
    post = post.replace('\u00f0\u009f\u008f\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0080', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0081', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0082', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0083', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0084', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0085', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0086', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0087', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0088', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0089', ' ')
    post = post.replace('\u00f0\u009f\u0090\u008a', ' ')
    post = post.replace('\u00f0\u009f\u0090\u008b', ' ')
    post = post.replace('\u00f0\u009f\u0090\u008f', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0090', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0093', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0095', ' ')
    post = post.replace('\u00f0\u009f\u0090\u0096', ' ')
    post = post.replace('\u00f0\u009f\u0090\u00aa', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u0091\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b6', ' ')
    post = post.replace('\u00f0\u009f\u0092\u00b7', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00af', ' ')
    post = post.replace('\u00f0\u009f\u0093\u00b5', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0080', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0081', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0082', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0084', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0085', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0086', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0087', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0089', ' ')
    post = post.replace('\u00f0\u009f\u0094\u0095', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00ac', ' ')
    post = post.replace('\u00f0\u009f\u0094\u00ad', ' ')
    post = post.replace('\u00f0\u009f\u0095\u009c', ' ')
    post = post.replace('\u00f0\u009f\u0095\u009d', ' ')
    post = post.replace('\u00f0\u009f\u0095\u009e', ' ')
    post = post.replace('\u00f0\u009f\u0095\u009f', ' ')
    post = post.replace('\u00f0\u009f\u0095\u00a0', ' ')
    post = post.replace('\u00f0\u009f\u0095\u00a1', ' ')
    post = post.replace('\u00f0\u009f\u0095\u00a2', ' ')
    post = post.replace('\u00f0\u009f\u0095\u00a3', ' ')
    post = post.replace('\u00f0\u009f\u0095\u00a4', ' ')
    post = post.replace('\u00f0\u009f\u0095\u00a5', ' ')
    post = post.replace('\u00f0\u009f\u0095\u00a6', ' ')
    post = post.replace('\u00f0\u009f\u0095\u00a7', ' ')
    return post

def emoticons_sentiment(post):
    if post != post.replace('\u00f0\u009f\u0091\u008e', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0091\u00b9', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0091\u00ba', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0091\u00bf', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0092\u0094', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0092\u00a2', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0092\u00a3', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0092\u00a5', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0092\u00a9', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u0090', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u0091', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u0092', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u0093', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u0094', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u0095', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u0096', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u009e', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u009f', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a0', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a1', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a2', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a3', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a4', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a5', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a6', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a7', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a8', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00a9', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00aa', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00ab', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00ac', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00ad', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00ae', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00af', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b0', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b1', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b2', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b3', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b5', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b6', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b7', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00bc', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00be', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0098\u00bf', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0099\u0080', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0099\u0088', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0099\u0089', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u0099\u008a', ' '):
        return "-1"
    elif post != post.replace('\u00e2\u0098\u0094', ' '):
        return "-1"
    elif post != post.replace('\u00f0\u009f\u008d\u0083', ' '):
        return "0"
    elif post != post.replace('\u00f0\u009f\u0098\u0088', ' '):
        return "0"
    elif post != post.replace('\u00f0\u009f\u0098\u008f', ' '):
        return "0"
    elif post != post.replace('\u00f0\u009f\u0098\u009b', ' '):
        return "0"
    elif post != post.replace('\u00f0\u009f\u0098\u009c', ' '):
        return "0"
    elif post != post.replace('\u00f0\u009f\u0098\u009d', ' '):
        return "0"
    elif post != post.replace('\u00f0\u009f\u0098\u00b4', ' '):
        return "0"
    elif post != post.replace('\u00f0\u009f\u008e\u0081', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u008e\u0086', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u008e\u0087', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u008e\u0089', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u008e\u008a', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0091\u008b', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0091\u008c', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0091\u008d', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0091\u008f', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u0085', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u008b', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u0093', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u0095', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u0096', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u0097', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u0098', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u0099', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u009a', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u009b', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u009c', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u009d', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u009e', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u009f', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0092\u00aa', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0080', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0081', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0082', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0083', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0084', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0085', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0086', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0087', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0089', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u008a', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u008b', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u008c', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u008d', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u008e', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0097', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0098', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u0099', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u009a', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b8', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u00b9', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u00ba', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u00bb', ' '):
        return "1"
    elif post != post.replace('\u00f0\u009f\u0098\u00bd', ' '):
        return "1"
    elif post != post.replace('\u00e2\u0098\u00ba', ' '):
        return "1"
    elif post != post.replace('\u00e2\u0099\u00a5', ' '):
        return "1"
    elif post != post.replace('\u00e2\u009c\u008c', ' '):
        return "1"
    else:
        return "none"






