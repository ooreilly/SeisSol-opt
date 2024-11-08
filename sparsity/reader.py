def readmatrix(filename, name, onlyones=True):
    """
    Read SeisSol sparse matrix format into a dense numpy matrix 

    Args:
        filename: Path to the file to xml file to read, e.g., "matrices_56.xml"
        name: Name of the matrix to read, e.g., "kDivMT(1)"
        onlyones(optional): If set to true, each non-zero is set to one. Otherwise, the
        actual value is used.

    Returns:
        A: A dense numpy matrix.
        nnz: The number of non-zeros

    """
    import xml.etree.ElementTree as ET
    import numpy as np
    root = ET.parse(filename).getroot()

    for tag in root.findall('matrix'):
        if name == tag.get('name'):
            columns = int(tag.get('columns'))
            rows = int(tag.get('rows'))
            entries = tag.findall('entry')
            A = np.zeros((rows, columns))
            i = 0
            nnz = 0
            for entry in entries:
                nnz += 1
                i = int(entry.get('row')) - 1
                j = int(entry.get('column')) - 1
                if onlyones:
                    val = 1
                else:
                    val = float(entry.get('value'))
                A[i,j] = val

            break

    return A, nnz



