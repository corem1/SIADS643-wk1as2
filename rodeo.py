def rename_rodeo_columns(columns):
    renamed_columns = []
    for col in columns:
        col = col.lower()
        col = col.replace(' ', '_')
        if col.endswith('_data'):
            col = col[:-5]
        renamed_columns.append(col)
    return renamed_columns


if __name__ == '__main__':
    # Create a list of exmple original column names
    original = [
        'Participant Count Data',
        'Rodeo Clown Count',
        'Hats Visible',
        'Cost Data',
    ]

    # Get the corrected column names
    corrected = rename_rodeo_columns(original)

    # Print a table to compare original and corrected names
    print('Original                  Corrected')
    print('--------                  ---------')
    for o, c in zip(original, corrected):
        print(f'{o:<25} {c:<25}')
