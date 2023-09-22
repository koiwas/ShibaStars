FROM node:14

# make app dir
WORKDIR /app

# npm install
COPY package*.json ./
RUN npm install

# copy other code
COPY . .

# start app
CMD ["npm", "start"]
