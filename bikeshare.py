"""Sources used:
    -Practice problems in project section
    -Python Pandas – Find the maximum value of a column and return its corresponding row values(Tutorials point site)
    -How do I get the row count of a Pandas DataFrame? (Stackoverflow)
    -Loop with df.head()(Stackoverflow)
    """


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Cities = ('chicago','new york city','washington')
months = ('january', 'february', 'march', 'april', 'may', 'june') 
days = ('saturday','sunday','monday','tuesday','wednesday','thursday','friday')
"""Global variables"""

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by
        (str) day - name of the day of week to filter by
    """
  
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    global city
    city = input("\nWhich city you wanna see its data? (Chicago,New york city, Washington)\n").lower()
    while city not in Cities:
          city = input('\nPlease pick one of the three cities or make sure of the spilling\n')
                
           
    month = input("\nWhich month - January, February, March, April, May, or June?\n").lower()
    while month not in months:
           month = input('\nPlease pick a month between Jan and June or chech your spelling\n')
            
               

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nWhich day you want its data?\n").lower()
    while day not in days:
         day = input('\nplease pick a day (check your spelling)\n')


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('\nThe selected month is: ', common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print('\nThe selected day is: ', common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print('\nThe Most common hour is: ', common_hour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe most common start station is: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most common End station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combined_stations = df.groupby(['End Station','Start Station']).count()
    print('\nThe most frequent combination of start station and end station trip is:', common_start_station,"and",common_end_station )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time in minutes is : ', total_travel_time / 60)
    print('\nTotal travel time in hours is : ', total_travel_time / 3060)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time in minutes is : ', mean_travel_time / 60)
    print('\nMean travel time in minutes is : ', mean_travel_time / 3600)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\nUser Type :', user_type)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nGender is:', gender)
    except KeyError:
        return('\nNo data Available\n')
        

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print('\nEarliest birth Year is: ',earliest_birth)

        recent_birth = df['Birth Year'].max()
        print('\nMost Recent birth Year is: ',recent_birth)

        common_birth = df['Birth Year'].mode()
        print('\nMost common Year is: ',earliest_birth)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw(df):
    i = 0
    e = 5    
    while(i < df.shape[0]):
        check = input(' \nWould you like to see raw data depending on your entries? Enter Yes or No)\n   ')
        if check == 'yes' :
            print(df.iloc[i:e])
            i+=5
            e+=5
        else :
             break
             



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
