from data_processor import reader, writer

data = reader.read_data('input.txt')
print(data)

writer.write_data(data, 'output.txt')