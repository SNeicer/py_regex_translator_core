from c_sharp_code_rewritten_in_python import interfaces

class TransformerCLI:

    def __init__(self, transformer: interfaces.IFileTransformer):
        self._transformer = transformer

    def run(self, args: list):
        sourcePath = args[0]
        targetPath = args[1]
        self._transformer.transform(sourcePath, targetPath)
