#! /bin/env/python

import pandas as pd


def get_ppls(output_file):
    train_all_ppl = []
    val_all_ppl = []
    test_all_ppl = []

    with open(output_file, 'r', encoding='utf-8') as training_output:
        train_dropout_ppl = []
        val_dropout_ppl = []
        for line in training_output:
            # If the training is finished...
            if 'End of training' in line:
                # Store the training perplexities of the specific dropout model in a list
                train_all_ppl.append(train_dropout_ppl)
                train_dropout_ppl = []
                # Store the validation perplexities of the specific dropout model in a list
                val_all_ppl.append(val_dropout_ppl)
                val_dropout_ppl = []
                # Append the test perplexity of the training process
                test_all_ppl.append(float(line.split(' ')[-1].strip('\n')))
            # If the second part of the batches is evaluated, store the training perplexity
            if '200/' in line:
                train_dropout_ppl.append(float(line.split(' ')[-1].strip('\n')))
            # If the epoch is finished, store the val ppl
            if 'end of epoch' in line:
                val_dropout_ppl.append(float(line.split(' ')[-1].strip('\n')))

    return train_all_ppl, val_all_ppl, test_all_ppl


def create_table(train, val, test):
    train_df = pd.DataFrame(train)
    train_df_transposed = train_df.transpose()
    # Name the rows and columns
    train_df_transposed.columns = ['dropout 0', 'dropout 0.3', 'dropout 0.5', 'dropout 0.7', 'dropout 1']
    train_df_transposed = train_df_transposed.rename(index=lambda x: 'Epoch ' + str(x+1))
    train_df_transposed.columns.name = "Train. perplexity"

    val_df = pd.DataFrame(val)
    val_df_transposed = val_df.transpose()
    # Name the rows and columns
    val_df_transposed.columns = ['dropout 0', 'dropout 0.3', 'dropout 0.5', 'dropout 0.7', 'dropout 1']
    val_df_transposed = val_df_transposed.rename(index=lambda x: 'Epoch ' + str(x + 1))
    val_df_transposed.columns.name = "Valid. perplexity"

    test_df = pd.DataFrame(test)
    test_df_transposed = test_df.transpose()
    # Name the rows and columns
    test_df_transposed.columns = ['dropout 0', 'dropout 0.3', 'dropout 0.5', 'dropout 0.7', 'dropout 1']
    test_df_transposed = test_df_transposed.rename(index=lambda x: 'Epoch ' + str(x+40))
    test_df_transposed.columns.name = "Test perplexity"

    return train_df_transposed, val_df_transposed, test_df_transposed


def create_chart(train, val):
    pass


def main():
    # Get all the perplexities for the generation of the table and the chart
    train_ppl, val_ppl, test_ppl = get_ppls('training_output.txt')

    # Create the table
    train_df, val_df, test_df = create_table(train_ppl, val_ppl, test_ppl)

    # Write data frames to csv file
    train_df.to_csv(r'perplexity_tables.csv', header=True, index_label='Train. perplexity')
    val_df.to_csv(r'perplexity_tables.csv', mode='a', header=True, index_label='Valid. perplexity')
    test_df.to_csv(r'perplexity_tables.csv', mode='a', header=True, index_label='Test perplexity')

    # Write data frames to excel file
    writer = pd.ExcelWriter('perplexity_tables.xlsx', engine='openpyxl')
    train_df.to_excel(writer, header=True, index_label='Train. perplexity', sheet_name='Train')
    val_df.to_excel(writer, header=True, index_label='Valid. perplexity', sheet_name='Val')
    test_df.to_excel(writer, header=True, index_label='Test perplexity', sheet_name='Test')
    writer.save()
    writer.close()

    # Create the line chart
    create_chart(train_ppl, val_ppl)


if __name__ == '__main__':
    main()