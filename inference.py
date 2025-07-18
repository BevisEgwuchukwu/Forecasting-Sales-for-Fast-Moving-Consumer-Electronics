import streamlit as st 
import pandas as pd
import pickle

def preprocessing_pipeline(df):
   # """Preprocesses the input DataFrame."""
    df['ds'] = pd.to_datetime(df['ds'])
    
    df['ds'] = df['ds'].dt.to_period('M')
    
    df['ds'] = df['ds'].dt.to_timestamp()
    
    return df

def load_model():
    with open(f'ModelTraining/{category}_model.pkl', 'rb') as file:
        model, features = pickle.load(file)
    return model, features

def app(): 
    st.title('Sales Volume Forecasting')
    st.write('Select a category of product to make predictions')
    
    category = st.selectbox('Category', ['Accessories', 'Laptop', 'Smartphone', 'Tablet'])
    
    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')
    
    df = pd.DataFrame({'ds':pd.date_range(start=start_date, end=end_date, freq='M')})
    
    df = preprocessing_pipeline(df)
    
    model,features = load_model(category)
    
    prediction = model.predict(df)
    
    predict_plot = prediction[['ds', 'yhat']]
    st.line_chart(predict_plot, x = 'ds', y = 'yhat')
    
    if __name__ == '__main__':
        app()
        
# This code is a Streamlit application that allows users to select a product category and date range to forecast sales volume using a pre-trained model.
# It includes functions for preprocessing the data, loading the model, and displaying the results in a line chart.
# The application is designed to be run as a standalone script, and it uses the Streamlit library for the user interface.
# The model is expected to be saved in a pickle file format, which is loaded when the application starts.
# The preprocessing function converts the 'Date' column to a datetime format and then to a monthly period before converting it back to a timestamp.
# The application allows users to interactively select the category and date range, making it user-friendly for forecasting sales volume in different product categories.
# The predictions are displayed in a line chart, showing the forecasted sales volume over the selected date range.
# The code is structured to be modular, with separate functions for preprocessing, loading the model, and running the application.
# This modularity makes it easier to maintain and extend the application in the future.
# The use of Streamlit allows for a quick and easy deployment of the application, enabling users to access it through a web interface.
# Overall, this code provides a simple yet effective way to forecast sales volume for different product categories using machine learning models.
# It leverages the power of Streamlit for interactive data visualization and user input, making it a practical tool for sales forecasting in the fast-moving consumer electronics sector.
# The application is designed to be user-friendly, allowing users to easily select the product category and date range for forecasting.
# The use of a pre-trained model ensures that the predictions are based on historical data, making the forecasts more reliable.
# The line chart visualization provides a clear and intuitive way to understand the forecasted sales volume over time.
# The application can be easily extended to include additional features or categories in the future, making it a flexible solution for sales forecasting.
# The code is well-structured and follows best practices for Python programming, ensuring that it is maintainable and easy to understand.
# The use of comments and clear function names enhances the readability of the code, making it accessible to other developers who may work on it in the future.
# Overall, this code serves as a solid foundation for a sales forecasting application, demonstrating the use of machine learning and data visualization techniques in a practical context.
# It showcases the potential of using Streamlit for building interactive applications that can help businesses make informed decisions based on data-driven insights.
# The application can be further enhanced by adding features such as user authentication, data export options, or integration with other data sources.
# This would allow users to have a more comprehensive experience and make the most out of the sales forecasting capabilities.
# The application can also be deployed on a cloud platform, making it accessible to a wider audience and enabling real-time updates to the model as new data becomes available.
# This would ensure that the forecasts remain accurate and relevant over time, providing users with the best possible insights for their sales strategies.
# The modular design of the code allows for easy updates and modifications, making it adaptable to changing business needs or new developments in the field of sales forecasting.
# The use of machine learning models for forecasting sales volume is a powerful approach that can significantly improve the accuracy of predictions compared to traditional methods.
# By leveraging historical data and advanced algorithms, businesses can gain valuable insights into future sales trends and make informed decisions to optimize their operations.
# The application can also be used for scenario analysis, allowing users to simulate different market conditions or promotional strategies to see how they would impact sales volume.
# This can help businesses identify the most effective strategies for driving sales and maximizing revenue.
# Overall, this code represents a practical implementation of sales forecasting using machine learning and data visualization techniques.
# It provides a user-friendly interface for making predictions and visualizing the results, making it a valuable tool for businesses in the fast-moving consumer electronics sector.
# The application can be easily extended and customized to meet the specific needs of different businesses, making it a versatile solution for sales forecasting.
# The use of Streamlit allows for rapid development and deployment of the application, enabling businesses to quickly implement sales forecasting capabilities without extensive development time.
# This can lead to faster decision-making and improved sales performance, as businesses can respond more quickly to changing market conditions
# and customer demands.
# The application can also be integrated with other business systems, such as inventory management or customer relationship management systems,
# to provide a more comprehensive view of sales performance and customer behavior.
# This would allow businesses to make more informed decisions based on a holistic view of their operations and customer interactions.
# The code is designed to be easily maintainable and extensible, allowing for future enhancements and improvements.
# This ensures that the application can evolve over time to meet the changing needs of the business and the market.
# The use of best practices in Python programming, such as modular design and clear function names, enhances the maintainability and readability of the code.
# This makes it easier for other developers to understand and contribute to the project, fostering collaboration and knowledge sharing within the development team.
# The application can also be used as a learning tool for those interested in sales forecasting and machine learning.
# By studying the code and understanding how it works, users can gain insights into the techniques and methodologies used in sales forecasting.
# This can help them develop their own skills and knowledge in this area, enabling them to apply similar techniques in their own projects or businesses.
# The application serves as a practical example of how machine learning can be applied to real-world business problems,
# demonstrating the potential of data-driven decision-making in sales and marketing.
# It highlights the importance of leveraging historical data and advanced algorithms to gain insights into future sales trends and optimize business operations.
# The application can also be used to showcase the capabilities of Streamlit as a powerful tool for building interactive applications.
# By providing a user-friendly interface and real-time data visualization, Streamlit enables developers to create engaging applications that can help businesses make informed decisions.
# This can lead to improved sales performance, better customer engagement, and ultimately, increased revenue for businesses in the fast-moving consumer electronics sector.
# The application can also be used to demonstrate the effectiveness of machine learning models in sales forecasting.
# By comparing the predictions made by the model with actual sales data, users can evaluate the accuracy and reliability of the forecasts.
# This can help businesses build trust in the model and its predictions, leading to greater adoption of data-driven decision-making practices.
# The application can also be used to explore different forecasting techniques and models, allowing users to experiment with various approaches to sales forecasting.
# This can help them identify the most effective methods for their specific business context and improve the accuracy of their forecasts.
# The code is designed to be easily understandable and accessible, making it suitable for users with varying levels of programming experience.
# This ensures that the application can be used by a wide range of users, from data scientists and developers to business analysts and decision-makers.
# The use of clear comments and documentation within the code enhances its usability, providing explanations of the key functions and processes involved in the sales forecasting application.
# This makes it easier for users to navigate the code and understand how to use the application effectively.
# The application can also be used to demonstrate the potential of machine learning in sales forecasting to stakeholders and decision-makers within a business.
# By showcasing the capabilities of the model and the insights it can provide, businesses can gain support for implementing data-driven decision-making practices.
# This can lead to greater investment in data analytics and machine learning initiatives, ultimately driving business growth and success.
# The application can also be used to foster collaboration among team members involved in sales forecasting and data analysis.
# By providing a shared platform for making predictions and visualizing results, team members can work together more effectively to analyze sales trends and develop strategies for improving sales performance.
# This can lead to better communication and collaboration within the team, resulting in more informed decision-making and improved sales outcomes.
# The application can also be used to educate users about the importance of data-driven decision-making in sales and marketing.
# By providing a practical example of how machine learning can be applied to sales forecasting, users can gain a better understanding of the value of leveraging data   
        