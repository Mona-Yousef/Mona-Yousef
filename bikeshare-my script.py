import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city =input('Would you like to see data for Chicago, New York city, or Washington?').lower()
        if city not in cities:
            print('unexpected input')
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','february','march','april','may','june']
    while True:
        month = input('Which month - January, February, March, April, May, June or all?').lower()
        if month not in months:
            print('unexpected input')
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?').lower()
        if day not in days:
            print('unexpected input')
        else:
            break


    print('-'*40)
    return city, month, day
####################################################################################################################3

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df1=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df1['Start Time'] = pd.to_datetime(df1['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df1['month'] = df1['Start Time'].dt.month
    df1['day_of_week'] = df1['Start Time'].dt.strftime("%A")

#                               #######################################################
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df1 = df1[df1['month'] == month]


        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df1 = df1[df1['day_of_week'] == day.title()]

    return df1

####################################################################################################################3

def time_stats(df1):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month=df1['month'].mode()[0]
    print('Most popular month is:{}'.format(months[popular_month-1]))

    # TO DO: display the most common day of week
    popular_day=df1['day_of_week'].mode()[0]
    print('Most popular day is:{}'.format(popular_day))


    # TO DO: display the most common start hour
    df1['hour'] = df1['Start Time'].dt.hour
    popular_hour = df1['hour'].mode()[0]
    print('Most Popular Start Hour:{}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

####################################################################################################################3

def station_stats(df1):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_StartStaion=df1['Start Station'].mode()[0]
    print('most popular start station is:{}'.format(popular_StartStaion))

    # TO DO: display most commonly used end station
    popular_EndStation=df1 ['End Station'].mode()[0]
    print('most popular end station is:{}.'.format(popular_EndStation))

    # TO DO: display most frequent combination of start station and end station trip
    most_frq_route= 'from' + df1['Start Station']+'to'+ df1 ['End Station']
    print('most frequent combination of start station and end station trip is:{}'.format(most_frq_route.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

####################################################################################################################3

def trip_duration_stats(df1):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is:{}'.format(df1['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('average travel time is:{}'.format(df1['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

####################################################################################################################3

def user_stats(df1):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:{}'.format(df1['User Type'].value_counts()))


    # TO DO: Display counts of gender
    if ('Gender' not in df1):
        print('NO Data Available for Washington')
    else:
        print('Counts of gender:{}'.format(df1['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Gender' not in df1):
        print('NO Data Available for Washington')
    else:
        print('earliest year is:{}'.format(df1['Birth Year'].max()))
        print('most recent year is:{}'.format(df1['Birth Year'].min()))
        print('most common year is:{}'.format(df1['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))


####################################################################################################################3
def display_data(df1):
    n=5
    print(df1.head(n))
    while True:
        mesaage=input('Do You Want to See 5 Rows of Data?  Enter yes or no.  ').lower()
        if mesaage =='no':
            break
        elif mesaage=='yes':
            n+=5
            print(df1.iloc[n - 5:n, :])
        else:
            print('unexpected input')




####################################################################################################################3

def main():
    while True:
        city, month, day = get_filters()
        df1 = load_data(city, month, day)

        time_stats(df1)
        station_stats(df1)
        trip_duration_stats(df1)
        user_stats(df1)
        display_data(df1)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
