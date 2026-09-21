import pandas as pd


# Load the 2019 and 2020 Divvy trip datasets
q1_2019 = pd.read_csv("Divvy_Trips_2019_Q1.csv")
q1_2020 = pd.read_csv("Divvy_Trips_2020_Q1.csv")


# Rename 2019 columns so both datasets use the same column names
q1_2019 = q1_2019.rename(columns={
    'trip_id': 'ride_id',
    'bikeid': 'rideable_type',
    'start_time': 'started_at',
    'end_time': 'ended_at',
    'from_station_name': 'start_station_name',
    'from_station_id': 'start_station_id',
    'to_station_name': 'end_station_name',
    'to_station_id': 'end_station_id',
    'usertype': 'member_casual'
})


# Check the structure and data types of both datasets
print("\nQ1 2019 Data Info:")
q1_2019.info()

print("\nQ1 2020 Data Info:")
q1_2020.info()


# Convert columns to the same data type before combining the datasets
q1_2019['ride_id'] = q1_2019['ride_id'].astype(str)
q1_2019['rideable_type'] = q1_2019['rideable_type'].astype(str)


# Combine the two datasets into one DataFrame
all_trips = pd.concat([q1_2019, q1_2020], ignore_index=True)


# Remove columns that are not available consistently in both datasets
all_trips = all_trips.drop(
    columns=[
        'start_lat',
        'start_lng',
        'end_lat',
        'end_lng',
        'birthyear',
        'gender',
        'tripduration'
    ],
    errors='ignore'
)


# Inspect the combined dataset
print("\nList of column names:\n", all_trips.columns)

print("\nHow many rows are in data frame?", len(all_trips))

print("\nDimensions of the data frame:", all_trips.shape)

print("\nSee the first 6 rows of data frame:\n", all_trips.head())

print("\nSee list of columns and data types:\n")
all_trips.info()

print("\nStatistical summary of data:\n", all_trips.describe())


# Check rider categories before cleaning
print(
    "\nValue counts for 'member_casual' column before cleaning:\n",
    all_trips['member_casual'].value_counts()
)


# Standardize rider categories into only member and casual
all_trips['member_casual'] = all_trips['member_casual'].replace({
    'Subscriber': 'member',
    'Customer': 'casual'
})


# Confirm that the rider categories were cleaned correctly
print(
    "\nValue counts for 'member_casual' column after cleaning:\n",
    all_trips['member_casual'].value_counts()
)


# Convert ride start and end times into datetime format
all_trips['started_at'] = pd.to_datetime(all_trips['started_at'])
all_trips['ended_at'] = pd.to_datetime(all_trips['ended_at'])


# Create new columns for date-based analysis
all_trips['date'] = all_trips['started_at'].dt.date
all_trips['month'] = all_trips['started_at'].dt.month
all_trips['day'] = all_trips['started_at'].dt.day
all_trips['year'] = all_trips['started_at'].dt.year
all_trips['day_of_week'] = all_trips['started_at'].dt.day_name()


# Calculate the duration of each ride in seconds
all_trips['ride_length'] = (
    all_trips['ended_at'] - all_trips['started_at']
).dt.total_seconds()


# Check the updated dataset after adding new columns
print("\nData types after adding date columns and ride_length:\n")
all_trips.info()


# Remove quality-control records and rides with invalid negative durations
all_trips_v2 = all_trips[
    (all_trips['start_station_name'] != "HQ QR")
    & (all_trips['ride_length'] >= 0)
].copy()


# Review overall ride duration statistics
print(
    "\nDescriptive statistics for ride_length:\n",
    all_trips_v2['ride_length'].describe()
)


# Compare ride duration statistics between casual riders and members
print(
    "\nRide length statistics grouped by member_casual:\n",
    all_trips_v2.groupby('member_casual')['ride_length']
    .agg(['mean', 'median', 'max', 'min'])
)


# Compare average ride duration by rider type and day of the week
print(
    "\nAverage ride length by member type and day of the week:\n",
    all_trips_v2.groupby(
        ['member_casual', 'day_of_week']
    )['ride_length'].mean()
)


# Set the days of the week in chronological order
days_order = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

all_trips_v2['day_of_week'] = pd.Categorical(
    all_trips_v2['day_of_week'],
    categories=days_order,
    ordered=True
)


# Run the weekday analysis again using the correct day order
print(
    "\nAverage ride length (sorted by day of week):\n",
    all_trips_v2.groupby(
        ['member_casual', 'day_of_week']
    )['ride_length'].mean()
)


# Create a summary table with ride counts and average ride duration
summary_stats = all_trips_v2.groupby(
    ['member_casual', 'day_of_week']
).agg(
    number_of_rides=('ride_id', 'count'),
    average_duration=('ride_length', 'mean')
).reset_index()


print(
    "\nSummary of rides and duration by rider type and weekday:\n",
    summary_stats
)


# Create a summary file for later visualization
counts = all_trips_v2.groupby(
    ['member_casual', 'day_of_week']
)['ride_length'].mean().reset_index()


# Export the summary results to CSV
counts.to_csv('avg_ride_length.csv', index=False)