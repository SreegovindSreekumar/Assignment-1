# Importing the required Python packages

import pandas as pd
import matplotlib.pyplot as plt

# Specifying the required column names and read the dataset using pandas"
# Note: 'Other Sales' corrected to 'Other_Sales' for consistency
# This assumes 'name', 'platform', 'EU_Sales', 'NA_Sales', 'Global_Sales', 'JP_Sales', 'Other_Sales' are valid column names.
drug_frequency = ['name', 'platform', 'EU_Sales',
                  'NA_Sales', 'Global_Sales', 'JP_Sales', 'Other_Sales']
video_games = pd.read_csv(
    "C:/Users/sreeg/Downloads/practical01/practical01/Video_Games_Sales_as_at_22_Dec_2016.csv")

# Selecting the first 10 games from the dataset
first_10_games = video_games.head(10)

# Calculating the NA sales for the first 10 games
# Filter games where NA_Sales is greater than 0
sales_in_NA = first_10_games[first_10_games["NA_Sales"] > 0]

# Group the sales data by the game's name and calculate the total NA sales for each game
NA_sales_by_game = sales_in_NA.groupby("Name")["NA_Sales"].sum()

# Filtering the data for the first 10 games with positive EU sales
sales_in_EU = first_10_games[first_10_games["EU_Sales"] > 0]

# Calculating the total EU sales for each game in the first 10 games
EU_sales_by_game = sales_in_EU.groupby("Name")["EU_Sales"].sum()

# Filtering the data for the first 10 games with positive JP sales
sales_in_JP = first_10_games[first_10_games["JP_Sales"] > 0]

# Calculating the total JP sales for each game in the first 10 games
JP_sales_by_game = sales_in_JP.groupby("Name")["JP_Sales"].sum()

# Filtering the data for the first 10 games with positive sales in other regions
sales_in_Other = first_10_games[first_10_games["Other_Sales"] > 0]

# Calculating the total sales in other regions for each game in the first 10 game
Other_sales_by_game = sales_in_Other.groupby("Name")["Other_Sales"].sum()

# Filtering the data for the first 10 games with positive global sales
sales_in_Global = first_10_games[first_10_games["Global_Sales"] > 0]

# Calculating the total global sales for each game in the first 10 games
Global_sales_by_game = sales_in_Global.groupby("Name")["Global_Sales"].sum()


# Fetching the data of Global sales on each platform"
global_sales_on_each_platform = video_games.groupby(
    "Platform")['Global_Sales'].sum().sort_values(ascending=False)

# Fetching the details of sales by first 10 games on other countries
Other_sales_by_game = first_10_games.groupby("Name")["Other_Sales"].sum()


# Function to Plot line graphs

def plotlinegraph(NA_Sales, EU_Sales):
    """
    Plotting Line Graph using the given data.

    Parameters:
    - NA_Sales: Pandas Series
        Sales data for each game in North America.
    - EU_Sales: Pandas Series
        Sales data for each game in Europe.

    Returns:
    None
    """
    # Set the title, x-axis label, y-axis label, and rotate x-axis labels for readability
    plt.plot(NA_Sales, color='#5865f2', label='Sales in NA')
    plt.plot(EU_Sales, color='#a60096', label='Sales in EU')
    plt.title("Sales of each game in NA and EU region")
    plt.xlabel("Game Name")
    plt.ylabel('Sales (in millions of units)')
    plt.legend()
    plt.xticks(rotation=90)
    # Display the plot line
    plt.show()

# Function to Bar chart graphs


def plotbar(global_sales_on_each_platform):
    """
    Plotting Bar Graph using the given data.

    Parameters:
    - global_sales_on_each_platform: Pandas Series
        Total global sales on each platform.

    Returns:
    None
    """
    # Set the size of the figure for better visualization
    plt.figure(figsize=(10, 6))

    # Plot a bar chart using the global sales data on each platform
    global_sales_on_each_platform.plot(kind='bar')

    # Set the title, x-axis label, y-axis label, and rotate x-axis labels for readability
    plt.title("Total global sales on each platform")
    plt.xlabel("Platform of the game")
    plt.ylabel("Total Global Sales (in millions of units)")
    plt.xticks(rotation=45)

    # Ensure the layout is tight
    plt.tight_layout()

    # Display the bar chart
    plt.show()


"Function to Pie chart"


def plotpie(Other_sales_by_game):
    """
    Plotting Pie Graph using the given data.

    Parameters:
    - Other_sales_by_game: Pandas Series
        The sales data for each game in other countries.

    Returns:
    None
    """
    # Set the title of the pie chart
    plt.title("Sales of each game in other countries")

    # Plot the pie chart using the sales data
    plt.pie(Other_sales_by_game,
            labels=Other_sales_by_game.index, autopct='%1.1f%%')

    # Display the pie chart
    plt.show()


# Call the function to plot the line graph
plotlinegraph(NA_sales_by_game, EU_sales_by_game)

# Call the function to plot the bar chart graph
plotbar(global_sales_on_each_platform)

# Call the function to plot the pie chart
plotpie(Other_sales_by_game)