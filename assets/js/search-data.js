// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-projects",
          title: "Projects",
          description: "A collection of boring projects.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "Repositories",
          description: "Boring repos",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "Listed in reversed chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-news",
          title: "News",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/news/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "A short CV. You can press the button on the right to view a full one.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "post-postgraduate-studies-at-sih",
        
          title: "Postgraduate studies at SIH",
        
        description: "Making right choices is crucial for your future career",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/postgraduate/";
          
        },
      },{id: "post-diet",
        
          title: "Diet",
        
        description: "Eating less and feeling more energetic",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/diet/";
          
        },
      },{id: "post-about-this-webpage",
        
          title: "About this webpage",
        
        description: "Why I am here",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/first-post/";
          
        },
      },{id: "news-i-am-thrilled-to-share-that-i-have-successfully-defended-my-phd-thesis-you-can-read-download-the-full-thesis-here-phd-thesis-pdf",
          title: 'I am thrilled to share that I have successfully defended my PhD thesis!...',
          description: "",
          section: "News",},{id: "news-i-have-secured-a-postdoctoral-research-position-at-shanghai-jiao-tong-university-following-the-successful-defense-of-my-phd-thesis",
          title: 'I have secured a postdoctoral research position at Shanghai Jiao Tong University following...',
          description: "",
          section: "News",},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%66%75%72%6B%68%64%61%6E%69%73%68@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/danishfurekhdar", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0003-4323-1135", "_blank");
        },
      },{
        id: 'social-researchgate',
        title: 'ResearchGate',
        section: 'Socials',
        handler: () => {
          window.open("https://www.researchgate.net/profile/Danish-Dar/", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=qOhxqbkAAAAJ", "_blank");
        },
      },{
        id: 'social-scopus',
        title: 'Scopus',
        section: 'Socials',
        handler: () => {
          window.open("https://www.scopus.com/authid/detail.uri?authorId=57219532607", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
